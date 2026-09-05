from django.db import transaction
from django.utils import timezone

from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from apps.notifications.models import Notification
from .models import Booking
from .serializers import BookingSerializer, AdminBookingSerializer,AdminCreateBookingSerializer

from apps.payments.models import Payment, PaymentLog
from apps.payments.utils import send_booking_confirmation


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {
            "request": self.request
        }

    def perform_create(self, serializer):
        serializer.save()


class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Booking.objects.filter(
            user=self.request.user
        )

        status_value = self.request.query_params.get(
            "status"
        )

        if status_value in [
            "pending",
            "confirmed",
            "cancelled",
        ]:
            queryset = queryset.filter(
                status=status_value
            )

        return queryset.order_by(
            "-created_at"
        )


class OfficeReservedDatesView(APIView):

    permission_classes = []

    def get(self, request, office_id):

        bookings = (
            Booking.objects
            .filter(
                office_id=office_id,
                status="confirmed"
            )
            .order_by("start_date")
            .values(
                "start_date",
                "end_date"
            )
        )

        return Response(
            list(bookings),
            status=status.HTTP_200_OK
        )


class AdminBookingListView(generics.ListAPIView):

    queryset = Booking.objects.all().order_by("-created_at")

    serializer_class = AdminBookingSerializer

    permission_classes = [IsAdminUser]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "user__username",
        "office__title",
        "office__city",
    ]

    ordering_fields = [
        "created_at",
        "start_date",
        "total_price",
    ]

    filterset_fields = [
        "status",
    ]


class AdminBookingDetailView(generics.RetrieveAPIView):

    queryset = Booking.objects.all()

    serializer_class = AdminBookingSerializer

    permission_classes = [IsAdminUser]


class AdminBookingStatusView(APIView):

    permission_classes = [IsAdminUser]

    def patch(self, request, pk):

        status_value = request.data.get(
            "status"
        )

        if status_value not in [
            "pending",
            "confirmed",
            "cancelled",
        ]:
            return Response(
                {
                    "error":
                        "Invalid booking status."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:

            with transaction.atomic():

                booking = (
                    Booking.objects
                    .select_for_update()
                    .select_related(
                        "user",
                        "office"
                    )
                    .get(pk=pk)
                )

                # ==========================================
                # CONFIRM BOOKING
                # ==========================================

                if status_value == "confirmed":

                    if booking.status == "cancelled":
                        return Response(
                            {
                                "error":
                                    "Cannot confirm a cancelled booking."
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    payment, created = Payment.objects.get_or_create(
                        booking=booking,
                        defaults={
                            "user": booking.user,
                            "amount": booking.total_price,
                            "currency": "MAD",
                            "status": Payment.STATUS_PENDING,
                            "payment_method": Payment.METHOD_CASH,
                        }
                    )

                    if payment.status != Payment.STATUS_PAID:

                        payment.status = Payment.STATUS_PAID
                        payment.payment_method = Payment.METHOD_CASH
                        payment.paid_at = timezone.now()

                        payment.save(
                            update_fields=[
                                "status",
                                "payment_method",
                                "paid_at",
                            ]
                        )

                        PaymentLog.objects.create(
                            payment=payment,
                            status=Payment.STATUS_PAID,
                            message=(
                                "Cash payment confirmed manually "
                                f"while confirming booking by admin "
                                f"{request.user.username}."
                            )
                        )

                    booking.status = "confirmed"

                    booking.save(
                        update_fields=[
                            "status"
                        ]
                    )

                # ==========================================
                # CANCEL BOOKING
                # ==========================================

                elif status_value == "cancelled":

                    if (
                        hasattr(booking, "payment") and
                        booking.payment.status == Payment.STATUS_PAID
                    ):
                        return Response(
                            {
                                "error":
                                    "A paid booking cannot be cancelled manually."
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )

                    old_status = booking.status

                    booking.status = "cancelled"

                    booking.save(
                        update_fields=[
                            "status"
                        ]
                    )

                    if old_status != "cancelled":

                        Notification.objects.create(
                            user=booking.user,
                            message=(
                                f"Your booking for "
                                f"{booking.office.title} "
                                f"from {booking.start_date} "
                                f"to {booking.end_date} "
                                f"has been cancelled by the administrator."
                            )
                        )

                # ==========================================
                # SET PENDING
                # ==========================================

                else:

                    booking.status = "pending"

                    booking.save(
                        update_fields=[
                            "status"
                        ]
                    )

        except Booking.DoesNotExist:

            return Response(
                {
                    "error":
                        "Booking not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        # ==========================================
        # SEND CONFIRMATION
        # ==========================================

        if status_value == "confirmed":

            send_booking_confirmation(
                booking.payment
            )

        return Response(
            {
                "message":
                    "Booking status updated successfully.",

                "status":
                    booking.status
            },
            status=status.HTTP_200_OK
        )

class AdminBookingDeleteView(
    generics.DestroyAPIView
):
    queryset = Booking.objects.all()
    serializer_class = AdminBookingSerializer
    permission_classes = [IsAdminUser]
    
    
class AdminCreateBookingView(
    generics.CreateAPIView
):

    serializer_class = (
        AdminCreateBookingSerializer
    )

    permission_classes = [
        IsAdminUser
    ]

    @transaction.atomic
    def perform_create(self, serializer):

        booking = serializer.save()

        Payment.objects.create(
            user=booking.user,
            booking=booking,
            amount=booking.total_price,
            currency="MAD",
            status=Payment.STATUS_PAID,
            payment_method=Payment.METHOD_CASH,
        )