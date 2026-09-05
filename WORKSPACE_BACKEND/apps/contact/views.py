from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .throttles import ContactThrottle
from .models import ContactMessage
from .serializers import (
    ContactCreateSerializer,
    ContactAdminSerializer,
    ContactReplySerializer,
    MyContactMessageSerializer
    
)
from .permissions import ContactPermission
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from apps.notifications.utils import send_notification_email
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.notifications.models import Notification
from apps.users.models import User

class ContactListView(generics.ListAPIView):

    queryset = ContactMessage.objects.all()

    serializer_class = ContactAdminSerializer

    permission_classes = [ContactPermission]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "email",
        "phone",
        "subject",
        "message",
    ]

    filterset_fields = [
        "status",
        "category",
    ]

    ordering_fields = [
        "created_at",
        "updated_at",
    ]

class ContactDetailView(generics.RetrieveAPIView):
    """
    Admin only
    """

    queryset = ContactMessage.objects.all()
    serializer_class = ContactAdminSerializer
    permission_classes = [ContactPermission]


class ContactCreateView(generics.CreateAPIView):

    queryset = ContactMessage.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ContactThrottle]

    def perform_create(self, serializer):

        if self.request.user.is_authenticated:

            serializer.save(
                user=self.request.user
            )

        else:

            serializer.save()


class ContactUpdateView(generics.UpdateAPIView):
    """
    Admin only
    """

    queryset = ContactMessage.objects.all()
    serializer_class = ContactAdminSerializer
    permission_classes = [ContactPermission]


class ContactDeleteView(generics.DestroyAPIView):
    """
    Admin only
    """

    queryset = ContactMessage.objects.all()
    serializer_class = ContactAdminSerializer
    permission_classes = [ContactPermission]
    
    
class ContactReplyView(APIView):

    permission_classes = [ContactPermission]

    def post(self, request, pk):

        # ==========================================
        # Get contact message
        # ==========================================

        try:
            contact = ContactMessage.objects.get(
                pk=pk
            )

        except ContactMessage.DoesNotExist:

            return Response(
                {
                    "error": "Message not found."
                },
                status=404
            )


        # ==========================================
        # Validate admin reply
        # ==========================================

        serializer = ContactReplySerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        reply = serializer.validated_data[
            "admin_reply"
        ]


        # ==========================================
        # Save admin reply
        # ==========================================

        contact.admin_reply = reply

        contact.status = (
            ContactMessage.Status.ANSWERED
        )

        contact.answered_by = request.user

        contact.answered_at = timezone.now()

        contact.save()


        # ==========================================
        # Find user
        # ==========================================

        notification_user = None


        # Preferred method:
        # contact is linked directly to user
        if contact.user:

            notification_user = contact.user


        # Fallback for old ContactMessage records
        # created before adding the user field
        else:

            notification_user = (
                User.objects
                .filter(
                    email__iexact=contact.email
                )
                .first()
            )


        # ==========================================
        # Create website notification
        # ==========================================

        if notification_user:

            Notification.objects.create(

                user=notification_user,

                message=(
                    f"Support replied to your message: "
                    f"“{contact.subject}”\n\n"
                    f"{reply}"
                )
            )


        # ==========================================
        # Send Email
        # ==========================================

        subject = f"Re: {contact.subject}"

        message = f"""
Hello {contact.name},

Thank you for contacting WorkSphere.

Your message:

{contact.message}

---

Our reply:

{reply}

---

Regards,
WorkSphere Support Team
"""

        send_notification_email(
            subject,
            message,
            contact.email
        )


        # ==========================================
        # Response
        # ==========================================

        return Response(
            {
                "message": "Reply sent successfully.",
                "notification_sent": (
                    notification_user is not None
                )
            }
        )
        
        
class MyContactMessagesView(generics.ListAPIView):

    serializer_class = MyContactMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return ContactMessage.objects.filter(
            user=self.request.user
        ).order_by("-created_at")