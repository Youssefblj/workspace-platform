from django.db import models

from apps.bookings.models import Booking
from apps.users.models import User


class Payment(models.Model):

    STATUS_PENDING = "pending"
    STATUS_PAID = "paid"
    STATUS_FAILED = "failed"

    STATUS = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PAID, "Paid"),
        (STATUS_FAILED, "Failed"),
    )

    METHOD_CASH = "cash"

    PAYMENT_METHODS = (
        (METHOD_CASH, "Cash"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name="payment"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="MAD"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=STATUS_PENDING
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHODS,
        default=METHOD_CASH
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"Payment #{self.id} - "
            f"{self.payment_method} - "
            f"{self.status}"
        )


class PaymentLog(models.Model):

    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        related_name="logs"
    )

    status = models.CharField(
        max_length=20
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.payment.id} - "
            f"{self.status}"
        )