from django.db import models
from django.conf import settings


class ContactMessage(models.Model):

    class Category(models.TextChoices):
        GENERAL = "general", "General Inquiry"
        BOOKING = "booking", "Booking"
        PAYMENT = "payment", "Payment"
        TECHNICAL = "technical", "Technical Support"
        COMPLAINT = "complaint", "Complaint"
        SUGGESTION = "suggestion", "Suggestion"

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In Progress"
        ANSWERED = "answered", "Answered"
        CLOSED = "closed", "Closed"
        
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contact_messages"
    )

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.GENERAL
    )

    subject = models.CharField(
        max_length=255
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )

    admin_reply = models.TextField(
        blank=True
    )

    answered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="answered_contact_messages"
    )

    answered_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject}"