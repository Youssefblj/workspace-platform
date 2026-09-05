from rest_framework import generics
from .models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser
from .serializers import (RegisterSerializer, UserSerializer,
                 ChangePasswordSerializer,ForgotPasswordSerializer, ResetPasswordSerializer,
                          ProfileUpdateSerializer,AdminUserSerializer,AdminUserUpdateSerializer)
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from django.core.mail import send_mail
from .models import User, PasswordResetCode
from apps.notifications.utils import send_notification_email
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser
)
from datetime import timedelta
from django.utils import timezone

class AdminUserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

#
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
#
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
# 
class ProfileUpdateView(generics.UpdateAPIView):
    serializer_class = (
        ProfileUpdateSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    parser_classes = [
        MultiPartParser,
        FormParser,
        JSONParser
    ]

    def get_object(self):
        return self.request.user
#   
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user

            if not user.check_password(
                serializer.validated_data['old_password']
            ):
                return Response(
                    {"error": "Wrong old password"},
                    status=400
                )

            user.set_password(
                serializer.validated_data['new_password']
            )
            user.save()

            # Send email notification
            if user.email:
                subject = "Password Changed Successfully"

                message = (
                    f"Hello {user.username},\n\n"
                    f"Your account password has been changed successfully.\n\n"
                    f"If this was not you, please contact support immediately."
                )

                send_notification_email(
                    subject,
                    message,
                    user.email
                )

            return Response({
                "message": "Password changed successfully"
            })

        return Response(serializer.errors, status=400)
    
class ForgotPasswordView(APIView):

    def post(self, request):

        serializer = ForgotPasswordSerializer(
            data=request.data
        )

        if serializer.is_valid():

            email = serializer.validated_data["email"]

            try:

                user = User.objects.get(
                    email=email
                )

            except User.DoesNotExist:

                return Response(
                    {
                        "error": "User not found"
                    },
                    status=404
                )

            # Delete old codes

            PasswordResetCode.objects.filter(
                user=user
            ).delete()

            code = str(
                random.randint(
                    100000,
                    999999
                )
            )

            PasswordResetCode.objects.create(
                user=user,
                code=code
            )

            send_mail(
                "Password Reset Code",
                f"Your reset code is: {code}",
                "noreply@example.com",
                [email],
                fail_silently=False,
            )

            return Response({
                "message":
                    "Reset code sent successfully"
            })

        return Response(
            serializer.errors,
            status=400
        ) 



class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']
            new_password = serializer.validated_data['new_password']

            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                return Response(
                    {"error": "User not found"},
                    status=404
                )

            reset_code = PasswordResetCode.objects.filter(
                user=user,
                code=code
            ).order_by("-created_at").first()

            if not reset_code:
                return Response(
                    {"error": "Invalid verification code"},
                    status=400
                )

            expiration_time = (
                reset_code.created_at
                + timedelta(minutes=10)
            )

            if timezone.now() > expiration_time:

                reset_code.delete()

                return Response(
                    {
                        "error":
                            "Verification code has expired. Request a new code."
                    },
                    status=400
                )

            user.set_password(new_password)
            user.save()

            PasswordResetCode.objects.filter(
                user=user
            ).delete()

            return Response({
                "message": "Password reset successful"
            })

        return Response(
            serializer.errors,
            status=400
        )
        
class DeleteMyAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):

        user = request.user

        user.delete()

        return Response(
            {
                "message": "Account deleted successfully."
            },
            status=200
        )
    
class AdminUsersListView(generics.ListAPIView):
    queryset = User.objects.all().order_by("-date_joined")

    serializer_class = AdminUserSerializer

    permission_classes = [IsAdminUser]

    pagination_class = AdminUserPagination

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "username",
        "email",
        "phone",
    ]
    
class AdminUserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    serializer_class = AdminUserSerializer

    permission_classes = [IsAdminUser]

    lookup_field = "id"
    
class AdminUserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()

    serializer_class = AdminUserUpdateSerializer

    permission_classes = [IsAdminUser]

    lookup_field = "id"
    
class AdminUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()

    permission_classes = [IsAdminUser]

    lookup_field = "id"
    
    
class AdminToggleUserActiveView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, id):
        user = User.objects.get(id=id)

        user.is_active = not user.is_active

        user.save()

        return Response({
            "message": "User status updated",
            "is_active": user.is_active
        })