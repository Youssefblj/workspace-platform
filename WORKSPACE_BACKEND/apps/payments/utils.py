from django.utils import timezone

from apps.notifications.models import Notification
from apps.notifications.utils import send_notification_email

from .models import Payment


def mark_payment_as_paid(payment):

    payment.status = Payment.STATUS_PAID
    payment.paid_at = timezone.now()

    payment.save(
        update_fields=[
            "status",
            "paid_at",
            "updated_at",
        ]
    )

    booking = payment.booking

    booking.status = "confirmed"

    booking.save(
        update_fields=[
            "status"
        ]
    )

    return payment


def send_booking_confirmation(payment):

    booking = payment.booking
    user = payment.user

    if (
        payment.status != Payment.STATUS_PAID or
        booking.status != "confirmed"
    ):
        return

    Notification.objects.create(
        user=user,
        message=(
            f"Your booking for {booking.office.title} "
            f"has been confirmed successfully."
        )
    )

    if user.email:

        subject = "Booking Confirmed"

        message = (
            f"Hello {user.username},\n\n"
            f"Your cash payment has been confirmed "
            f"and your booking is now confirmed.\n\n"

            f"Office: {booking.office.title}\n"
            f"City: {booking.office.city}\n"
            f"Start Date: {booking.start_date}\n"
            f"End Date: {booking.end_date}\n"
            f"Total Price: {payment.amount} MAD\n"
            f"Payment Method: Cash\n"
            f"Payment Status: Paid\n"
            f"Booking Status: Confirmed\n\n"

            f"Thank you for using WorkSphere."
        )

        send_notification_email(
            subject,
            message,
            user.email
        )