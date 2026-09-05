from django.db import transaction

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import filters
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
from rest_framework.response import Response


from .models import (
    Payment,
    PaymentLog
)

from .serializers import (
    PaymentSerializer,
    CashPaymentRequestSerializer
)

from .utils import (
    mark_payment_as_paid,
    send_booking_confirmation,
)

from apps.bookings.models import Booking
from apps.notifications.utils import send_notification_email
from apps.contact.models import ContactMessage


# ==========================================================
# Helpers
# ==========================================================

def get_user_booking(request, booking_id):

    try:
        return Booking.objects.get(
            id=booking_id,
            user=request.user
        )

    except Booking.DoesNotExist:
        return None


def get_or_create_payment(
    booking,
    user
):

    payment, created = Payment.objects.get_or_create(
        booking=booking,
        defaults={
            "user": user,
            "amount": booking.total_price,
            "currency": "MAD",
            "status": Payment.STATUS_PENDING,
            "payment_method": Payment.METHOD_CASH,
        }
    )

    return payment, created


# ==========================================================
# CASH PAYMENT
# ==========================================================

class CashPaymentView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request, booking_id):

        booking = get_user_booking(
            request,
            booking_id
        )

        if not booking:
            return Response(
                {
                    "error": "Booking not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if booking.status == "confirmed":
            return Response(
                {
                    "error":
                        "This booking is already confirmed."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if booking.status == "cancelled":
            return Response(
                {
                    "error":
                        "This booking has been cancelled."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ==============================================
        # Validate Cash Form
        # ==============================================

        serializer = CashPaymentRequestSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        full_name = serializer.validated_data[
            "full_name"
        ]

        phone = serializer.validated_data[
            "phone"
        ]

        note = serializer.validated_data.get(
            "note",
            ""
        )

        if not request.user.email:
            return Response(
                {
                    "error":
                        "Your account must have an email address."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # ==============================================
        # Contact Message
        # ==============================================

        contact_subject = (
            f"Cash Payment Request - Booking #{booking.id}"
        )

        contact_message = (
            f"Cash payment request for booking #{booking.id}.\n\n"

            f"Customer: {full_name}\n"
            f"Email: {request.user.email}\n"
            f"Phone: {phone}\n\n"

            f"Workspace: {booking.office.title}\n"
            f"City: {booking.office.city}\n"

            f"Booking ID: {booking.id}\n"
            f"Start Date: {booking.start_date}\n"
            f"End Date: {booking.end_date}\n"

            f"Amount: {booking.total_price} MAD\n\n"

            f"Payment Method: Cash\n"
            f"Payment Status: Pending\n"
            f"Booking Status: Pending\n\n"

            f"Customer Note:\n"
            f"{note if note else 'No additional note.'}"
        )

        # ==============================================
        # Save
        # ==============================================

        with transaction.atomic():

            payment, created = get_or_create_payment(
                booking,
                request.user
            )

            if (
                payment.status ==
                Payment.STATUS_PAID
            ):
                return Response(
                    {
                        "error":
                            "This booking has already been paid."
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            payment.payment_method = (
                Payment.METHOD_CASH
            )

            payment.status = (
                Payment.STATUS_PENDING
            )

            payment.paid_at = None

            payment.save(
                update_fields=[
                    "payment_method",
                    "status",
                    "paid_at",
                    "updated_at",
                ]
            )

            booking.status = "pending"

            booking.save(
                update_fields=[
                    "status"
                ]
            )

            PaymentLog.objects.create(
                payment=payment,
                status=Payment.STATUS_PENDING,
                message=(
                    "Cash payment request submitted. "
                    "Waiting for admin confirmation."
                )
            )

            existing_contact = (
                ContactMessage.objects
                .filter(
                    user=request.user,
                    category=ContactMessage.Category.PAYMENT,
                    subject=contact_subject,
                )
                .first()
            )

            if existing_contact:

                existing_contact.name = full_name
                existing_contact.email = request.user.email
                existing_contact.phone = phone
                existing_contact.message = contact_message
                existing_contact.status = (
                    ContactMessage.Status.NEW
                )

                existing_contact.save()

                contact = existing_contact

            else:

                contact = ContactMessage.objects.create(
                    user=request.user,
                    name=full_name,
                    email=request.user.email,
                    phone=phone,
                    category=(
                        ContactMessage.Category.PAYMENT
                    ),
                    subject=contact_subject,
                    message=contact_message,
                    status=(
                        ContactMessage.Status.NEW
                    ),
                )

        # ==============================================
        # Email User
        # ==============================================

        subject = (
            "Cash Payment Request Received"
        )

        message = (
            f"Hello {full_name},\n\n"

            f"We received your cash payment request.\n\n"

            f"Workspace: {booking.office.title}\n"
            f"Booking ID: {booking.id}\n"

            f"Amount due: {payment.amount} MAD\n"

            f"Payment Method: Cash\n"
            f"Payment Status: Pending\n"
            f"Booking Status: Pending\n\n"

            f"Your booking will be confirmed "
            f"after an administrator verifies "
            f"your cash payment.\n\n"

            f"You will receive a notification "
            f"when the payment is confirmed.\n\n"

            f"Thank you for using WorkSphere."
        )

        send_notification_email(
            subject,
            message,
            request.user.email
        )

        return Response(
            {
                "message":
                    "Cash payment request sent successfully. "
                    "Waiting for admin confirmation.",

                "payment":
                    PaymentSerializer(
                        payment,
                        context={
                            "request": request
                        }
                    ).data,

                "booking_status":
                    booking.status,

                "contact": {
                    "id": contact.id,
                    "subject": contact.subject,
                    "category": contact.category,
                    "status": contact.status,
                }
            },
            status=status.HTTP_200_OK
        )


# ==========================================================
# MY PAYMENTS
# ==========================================================

class MyPaymentsView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        payments = (
            Payment.objects
            .filter(
                user=request.user
            )
            .select_related(
                "booking",
                "booking__office"
            )
            .order_by(
                "-created_at"
            )
        )

        serializer = PaymentSerializer(
            payments,
            many=True,
            context={
                "request": request
            }
        )

        return Response(
            serializer.data
        )


# ==========================================================
# ADMIN PAYMENT LIST
# ==========================================================

class AdminPaymentListView(
    generics.ListAPIView
):

    queryset = (
        Payment.objects
        .select_related(
            "user",
            "booking",
            "booking__office"
        )
        .order_by(
            "-created_at"
        )
    )

    serializer_class = (
        PaymentSerializer
    )

    permission_classes = [
        IsAdminUser
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "currency",
        "payment_method",
    ]

    search_fields = [
        "user__username",
        "user__email",
        "booking__office__title",
        "booking__office__city",
    ]

    ordering_fields = [
        "created_at",
        "amount",
        "paid_at",
    ]


# ==========================================================
# ADMIN PAYMENT DETAIL
# ==========================================================

class AdminPaymentDetailView(
    generics.RetrieveAPIView
):

    queryset = (
        Payment.objects
        .select_related(
            "user",
            "booking",
            "booking__office"
        )
    )

    serializer_class = (
        PaymentSerializer
    )

    permission_classes = [
        IsAdminUser
    ]


# ==========================================================
# ADMIN CONFIRM CASH PAYMENT
# ==========================================================

class AdminConfirmCashPaymentView(APIView):

    permission_classes = [
        IsAdminUser
    ]

    def post(self, request, pk):

        try:

            with transaction.atomic():

                payment = (
                    Payment.objects
                    .select_for_update()
                    .select_related(
                        "user",
                        "booking",
                        "booking__office"
                    )
                    .get(pk=pk)
                )

                if (
                    payment.payment_method !=
                    Payment.METHOD_CASH
                ):
                    return Response(
                        {
                            "error":
                                "Only cash payments can be confirmed manually."
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                if (
                    payment.status ==
                    Payment.STATUS_PAID
                ):
                    return Response(
                        {
                            "error":
                                "This payment has already been confirmed."
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                if (
                    payment.booking.status ==
                    "cancelled"
                ):
                    return Response(
                        {
                            "error":
                                "Cannot confirm payment for a cancelled booking."
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                payment = mark_payment_as_paid(
                    payment
                )

                PaymentLog.objects.create(
                    payment=payment,
                    status=Payment.STATUS_PAID,
                    message=(
                        "Cash payment confirmed manually "
                        f"by admin {request.user.username}."
                    )
                )

            send_booking_confirmation(
                payment
            )

            return Response(
                {
                    "message":
                        "Cash payment confirmed successfully.",

                    "payment":
                        PaymentSerializer(
                            payment,
                            context={
                                "request": request
                            }
                        ).data
                },
                status=status.HTTP_200_OK
            )

        except Payment.DoesNotExist:

            return Response(
                {
                    "error":
                        "Payment not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )