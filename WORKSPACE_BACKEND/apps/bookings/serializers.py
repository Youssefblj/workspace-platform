import datetime
from rest_framework import serializers
from .models import Booking
from datetime import date
from apps.users.serializers import UserSerializer
from apps.offices.serializers import OfficeSerializer
from decimal import Decimal, ROUND_UP

from apps.users.models import User
from apps.offices.models import Office
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user', 'total_price']

    def validate(self, data):
        start = data['start_date']
        end = data['end_date']
        office = data['office']
        
        
        today = date.today()

        if start < today:
            raise serializers.ValidationError(
            "Start date cannot be in the past."
        )
        if end < start:
            raise serializers.ValidationError(
                "End date must be after start date"
            )

        overlapping = Booking.objects.filter(
            office=office,
            start_date__lte=end,
            end_date__gte=start,
            status='confirmed'
        ).exists()

        if overlapping:
            raise serializers.ValidationError(
                "This office is already booked for these dates."
            )

        return data

    def create(self, validated_data):
        user = self.context['request'].user
        office = validated_data['office']

        start = validated_data['start_date']
        end = validated_data['end_date']

        duration = (end - start).days + 1

        if office.rent_type == 'daily':
            total = office.price * duration
        elif office.rent_type == 'weekly':
            weeks = max(1, duration / 7)
            total = office.price * weeks
        else:
            months = max(1, duration / 30)
            total = office.price * months

        booking = Booking.objects.create(
            user=user,
            total_price=total,
            **validated_data
        )

        return booking
class AdminBookingSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    office = OfficeSerializer(read_only=True)

    class Meta:
        model = Booking

        fields = "__all__"
        



class AdminCreateBookingSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(
            is_active=True,
            is_staff=False
        )
    )

    office = serializers.PrimaryKeyRelatedField(
        queryset=Office.objects.all()
    )

    class Meta:
        model = Booking

        fields = [
            "id",
            "user",
            "office",
            "start_date",
            "end_date",
            "total_price",
            "status",
        ]

        read_only_fields = [
            "id",
            "total_price",
            "status",
        ]

    def validate(self, data):

        start = data["start_date"]
        end = data["end_date"]
        office = data["office"]

        today = date.today()

        if start < today:
            raise serializers.ValidationError({
                "start_date":
                    "Start date cannot be in the past."
            })

        if end < start:
            raise serializers.ValidationError({
                "end_date":
                    "End date must be after or equal to start date."
            })

        overlapping = Booking.objects.filter(
            office=office,
            start_date__lte=end,
            end_date__gte=start,
            status="confirmed"
        ).exists()

        if overlapping:
            raise serializers.ValidationError({
                "office":
                    "This office is already booked for these dates."
            })

        return data

    def create(self, validated_data):

        office = validated_data["office"]

        start = validated_data["start_date"]
        end = validated_data["end_date"]

        duration = (
            end - start
        ).days + 1

        price = Decimal(
            str(office.price)
        )

        if office.rent_type == "daily":

            total = (
                price *
                Decimal(duration)
            )

        elif office.rent_type == "weekly":

            weeks = (
                Decimal(duration) /
                Decimal("7")
            ).quantize(
                Decimal("1"),
                rounding=ROUND_UP
            )

            total = price * weeks

        else:

            months = (
                Decimal(duration) /
                Decimal("30")
            ).quantize(
                Decimal("1"),
                rounding=ROUND_UP
            )

            total = price * months

        booking = Booking.objects.create(
            total_price=total,
            status="confirmed",
            **validated_data
        )

        return booking