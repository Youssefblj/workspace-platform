from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    user_profile_image = serializers.ImageField(
        source="user.profile_image",
        read_only=True
    )

    office_title = serializers.CharField(
        source="office.title",
        read_only=True
    )

    class Meta:
        model = Review

        fields = [
            "id",
            "user",
            "username",
            "user_profile_image",
            "office",
            "office_title",
            "rating",
            "comment",
            "created_at"
        ]

        read_only_fields = [
            "user",
            "username",
            "user_profile_image",
            "office_title"
        ]