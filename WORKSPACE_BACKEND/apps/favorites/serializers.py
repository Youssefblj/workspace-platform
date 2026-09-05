from rest_framework import serializers
from .models import Favorite
from apps.offices.serializers import OfficeSerializer


class FavoriteSerializer(serializers.ModelSerializer):

    office_details = OfficeSerializer(
        source="office",
        read_only=True
    )

    class Meta:
        model = Favorite

        fields = [
            "id",
            "office",
            "office_details",
            "created_at"
        ]

        read_only_fields = [
            "id",
            "created_at"
        ]