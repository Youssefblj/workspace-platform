from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import NotificationAdminPermission
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        ).order_by('-created_at')


class NotificationReadView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        )

    def perform_update(self, serializer):
        serializer.save(is_read=True)


class UnreadNotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).count()

        return Response({
            "unread_count": count
        })
        
class MarkAllNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        updated = Notification.objects.filter(
            user=request.user,
            is_read=False
        ).update(is_read=True)

        return Response({
            "message": "All notifications marked as read",
            "updated_count": updated
        })
        
        
        
class AdminNotificationListView(generics.ListAPIView):

    queryset = Notification.objects.select_related("user")

    serializer_class = NotificationSerializer

    permission_classes = [NotificationAdminPermission]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = [
    "is_read"
    ]

    search_fields = [
        "message",
        "user__username"
    ]

    ordering_fields = [
        "created_at"
    ]
class AdminNotificationDetailView(generics.RetrieveAPIView):

    queryset = Notification.objects.select_related("user")

    serializer_class = NotificationSerializer

    permission_classes = [NotificationAdminPermission]
class AdminNotificationDeleteView(generics.DestroyAPIView):

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer

    permission_classes = [NotificationAdminPermission]
    
class AdminSendNotificationView(APIView):

    permission_classes = [NotificationAdminPermission]

    def post(self, request):

        user_id = request.data.get("user")

        message = request.data.get("message")

        if not user_id or not message:

            return Response(
                {
                    "error": "User and message are required."
                },
                status=400
            )

        from apps.users.models import User

        try:

            user = User.objects.get(id=user_id)

        except User.DoesNotExist:

            return Response(
                {
                    "error": "User not found."
                },
                status=404
            )

        notification = Notification.objects.create(
            user=user,
            message=message
        )

        serializer = NotificationSerializer(notification)

        return Response(serializer.data)