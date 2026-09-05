from rest_framework import serializers
from .models import ContactMessage
import re



class ContactCreateSerializer(serializers.ModelSerializer):
    """
    Serializer used by visitors/users
    to submit a contact message.
    """

    class Meta:
        model = ContactMessage

        fields = (
            "id",
            "name",
            "email",
            "phone",
            "category",
            "subject",
            "message",
            "created_at",
        )

        read_only_fields = (
            "id",
            "user",
            "created_at",
        )

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "Name must contain at least 3 characters."
            )

        return value

    def validate_phone(self, value):
        if not value:
            return value

        value = value.strip()

        pattern = r"^\+?[0-9]{8,20}$"

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        return value

    def validate_subject(self, value):
        value = value.strip()

        if len(value) < 5:
            raise serializers.ValidationError(
                "Subject must contain at least 5 characters."
            )

        return value

    def validate_message(self, value):
        value = value.strip()

        if len(value) < 15:
            raise serializers.ValidationError(
                "Please provide more details in your message."
            )

        return value

    def validate(self, attrs):
        """
        Global validation and data normalization.
        """

        # Normalize text fields
        attrs["name"] = attrs["name"].strip()
        attrs["email"] = attrs["email"].strip().lower()
        attrs["subject"] = attrs["subject"].strip()
        attrs["message"] = attrs["message"].strip()

        if attrs.get("phone"):
            attrs["phone"] = attrs["phone"].strip()

        # Prevent identical subject and message
        if attrs["subject"].lower() == attrs["message"].lower():
            raise serializers.ValidationError(
                {
                    "message": "Message cannot be identical to the subject."
                }
            )

        return attrs
    
class MyContactMessageSerializer(serializers.ModelSerializer):

    answered_by = serializers.StringRelatedField(
        read_only=True
    )

    class Meta:
        model = ContactMessage

        fields = (
            "id",
            "category",
            "subject",
            "message",
            "status",
            "admin_reply",
            "answered_by",
            "answered_at",
            "created_at",
            "updated_at",
        )

        read_only_fields = fields

class ContactAdminSerializer(serializers.ModelSerializer):

    answered_by = serializers.StringRelatedField(
        read_only=True
    )

    user_profile_image = serializers.SerializerMethodField()

    class Meta:
        model = ContactMessage

        fields = [
            "id",
            "user",
            "name",
            "email",
            "phone",
            "category",
            "subject",
            "message",
            "status",
            "admin_reply",
            "answered_by",
            "answered_at",
            "created_at",
            "updated_at",
            "user_profile_image",
        ]

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "answered_at",
            "answered_by",
            "user_profile_image",
        )

    def get_user_profile_image(self, obj):

        if (
            obj.user and
            obj.user.profile_image
        ):
            request = self.context.get("request")

            url = obj.user.profile_image.url

            if request:
                return request.build_absolute_uri(url)

            return url

        return None
        
class ContactReplySerializer(serializers.Serializer):
    admin_reply = serializers.CharField()

    def validate_admin_reply(self, value):
        value = value.strip()

        if len(value) < 10:
            raise serializers.ValidationError(
                "Reply must contain at least 10 characters."
            )

        return value