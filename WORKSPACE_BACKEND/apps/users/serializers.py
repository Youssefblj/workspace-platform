from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
import re

def validate_international_phone(value):
    if not value:
        raise serializers.ValidationError(
            "Phone number is required."
        )

    value = value.strip()

    # Remove spaces, -, (, )
    value = re.sub(r"[\s\-\(\)]", "", value)

    if not re.fullmatch(
        r"\+[1-9]\d{7,14}",
        value
    ):
        raise serializers.ValidationError(
            "Enter a valid international phone number."
        )

    return value

class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        max_length=30,
        error_messages={
            "invalid": "Enter a valid email address.",
            "max_length": "Email cannot exceed 30 characters."
        }
    )

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        max_length=20,
        validators=[validate_password],
        error_messages={
            "min_length": "Password must contain at least 8 characters.",
            "max_length": "Password cannot exceed 20 characters."
        }
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "password",
        ]

    def validate_username(self, value):

        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "Username must contain at least 3 characters."
            )

        if len(value) > 14:
            raise serializers.ValidationError(
                "Username cannot exceed 14 characters."
            )

        if not re.fullmatch(r"[A-Za-z]+", value):
            raise serializers.ValidationError(
                "Username must contain letters only."
            )

        if User.objects.filter(
            username__iexact=value
        ).exists():
            raise serializers.ValidationError(
                "This username is already taken."
            )

        return value

    def validate_email(self, value):

        value = value.strip().lower()
        
        if len(value) > 30:
            raise serializers.ValidationError(
                "Email cannot exceed 30 characters."
            )

        if User.objects.filter(
            email__iexact=value
        ).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )

        return value

    def validate_phone(self, value):
        return validate_international_phone(value)

    def create(self, validated_data):

        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone',"profile_image",'is_staff', 'is_active','date_joined']

#password change serializer

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=30
    )


class ResetPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField(
        max_length=30,
        required=True,
    )

    code = serializers.CharField(
        min_length=6,
        max_length=6,
        required=True,
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
        max_length=20,
        required=True,
        validators=[validate_password],
        error_messages={
            "min_length": "Password must contain at least 8 characters.",
            "max_length": "Password cannot exceed 20 characters."
        }
    )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    profile_image = serializers.ImageField(
        required=False,
        allow_null=True)
    class Meta:
        model = User
        fields = ["username", "email", "phone","profile_image"]

    def validate_username(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Username must contain at least 3 characters."
            )

        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                "This username is already taken."
            )

        return value

    def validate_email(self, value):

        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )

        return value

    def validate_phone(self, value):
        if not value:
           return value

        return validate_international_phone(value)
    
    
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "profile_image",
            "is_staff",
            "is_active",
            "date_joined",
        ]
        
class AdminUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "is_active",
        ]

    def validate_username(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Username must contain at least 3 characters."
            )

        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(
            username=value
        ).exists():
            raise serializers.ValidationError(
                "This username is already taken."
            )

        return value

    def validate_email(self, value):

        user = self.instance

        if User.objects.exclude(pk=user.pk).filter(
            email=value
        ).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )

        return value

  
    def validate_phone(self, value):
        if not value:
           return value

        return validate_international_phone(value)
    
    