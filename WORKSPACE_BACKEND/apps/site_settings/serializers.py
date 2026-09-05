from rest_framework import serializers
import re

from .models import SiteSettings


def validate_international_phone(value):

    if not value:
        return value

    value = value.strip()

    value = re.sub(
        r"[\s\-\(\)]",
        "",
        value
    )

    if not re.fullmatch(
        r"\+[1-9]\d{7,14}",
        value
    ):
        raise serializers.ValidationError(
            "Enter a valid international phone number."
        )

    return value


class SiteSettingsSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = SiteSettings

        fields = [
            "id",
            "website_name",
            "website_url",
            "contact_email",
            "contact_phone",
            "whatsapp_number",
            "address",
            "instagram_url",
            "facebook_url",
            "linkedin_url",
            "twitter_url",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "updated_at",
        ]

    def validate_contact_phone(
        self,
        value
    ):
        return validate_international_phone(
            value
        )

    def validate_whatsapp_number(
        self,
        value
    ):
        return validate_international_phone(
            value
        )