from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    user_profile_image = serializers.ImageField(
        source="user.profile_image",
        read_only=True
    )

    class Meta:
        model = Notification

        fields = [
            "id",
            "user",
            "username",
            "user_profile_image",
            "message",
            "is_read",
            "created_at"
        ]