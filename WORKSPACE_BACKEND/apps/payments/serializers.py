from rest_framework import serializers
import re

from .models import Payment


# ==========================================================
# CASH PAYMENT REQUEST
# ==========================================================

class CashPaymentRequestSerializer(
    serializers.Serializer
):

    full_name = serializers.CharField(
        max_length=150
    )

    phone = serializers.CharField(
        max_length=20
    )

    note = serializers.CharField(
        max_length=500,
        required=False,
        allow_blank=True
    )

    def validate_full_name(self, value):

        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "Full name must contain at least 3 characters."
            )

        return value

    def validate_phone(self, value):

        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Phone number is required."
            )

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

    def validate_note(self, value):

        return value.strip()


# ==========================================================
# PAYMENT SERIALIZER
# ==========================================================

class PaymentSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    user_email = serializers.EmailField(
        source="user.email",
        read_only=True
    )
    
    user_profile_image = serializers.ImageField(
        source="user.profile_image",
        read_only=True
    )

    office_title = serializers.CharField(
        source="booking.office.title",
        read_only=True
    )

    office_city = serializers.CharField(
        source="booking.office.city",
        read_only=True
    )

    office_image = serializers.SerializerMethodField()

    start_date = serializers.DateField(
        source="booking.start_date",
        read_only=True
    )

    end_date = serializers.DateField(
        source="booking.end_date",
        read_only=True
    )

    invoice_number = serializers.SerializerMethodField()

    duration = serializers.SerializerMethodField()

    class Meta:
        model = Payment

        fields = [
            "id",

            "username",
            "user_email",

            "user",
            "booking",
            "user_profile_image",


            "amount",
            "currency",

            "status",
            "payment_method",

            "office_title",
            "office_city",
            "office_image",

            "start_date",
            "end_date",
            "duration",

            "invoice_number",

            "paid_at",
            "created_at",
            "updated_at",
        ]

        read_only_fields = fields

    def get_invoice_number(self, obj):

        return f"INV-{obj.id:06d}"

    def get_duration(self, obj):

        if (
            obj.booking.start_date and
            obj.booking.end_date
        ):

            return (
                obj.booking.end_date -
                obj.booking.start_date
            ).days + 1

        return 0

    def get_office_image(self, obj):

        image = (
            obj.booking.office.images
            .order_by(
                "-is_primary",
                "id"
            )
            .first()
        )

        if not image:
            return None

        request = self.context.get(
            "request"
        )

        if request:
            return request.build_absolute_uri(
                image.image.url
            )

        return image.image.url