from rest_framework import serializers
from django.db.models import Avg

from .models import Office, OfficeImage


class OfficeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeImage
        fields = [
            "id",
            "image",
            "is_primary",
        ]


class OfficeSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = "__all__"

    def get_images(self, obj):

        images = obj.images.order_by(
            "-is_primary",
            "id"
        )

        return OfficeImageSerializer(
            images,
            many=True
        ).data

    def get_average_rating(self, obj):

        avg = obj.reviews.aggregate(
            avg=Avg("rating")
        )["avg"]

        return round(avg, 1) if avg else 0


class AdminOfficeSerializer(serializers.ModelSerializer):

    images = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = "__all__"

    def get_images(self, obj):

        images = obj.images.order_by(
            "-is_primary",
            "id"
        )

        return OfficeImageSerializer(
            images,
            many=True
        ).data

    def get_average_rating(self, obj):

        avg = obj.reviews.aggregate(
            avg=Avg("rating")
        )["avg"]

        return round(avg, 1) if avg else 0