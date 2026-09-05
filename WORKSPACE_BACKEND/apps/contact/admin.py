from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "category",
        "colored_status",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    ordering = ("-created_at",)

    list_per_page = 20

    readonly_fields = (
        "created_at",
        "updated_at",
        "answered_at",
        "answered_by",
    )

    fieldsets = (

        (
            "Contact Information",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                )
            },
        ),

        (
            "Message",
            {
                "fields": (
                    "category",
                    "subject",
                    "message",
                )
            },
        ),

        (
            "Administration",
            {
                "fields": (
                    "status",
                    "admin_reply",
                    "answered_by",
                    "answered_at",
                )
            },
        ),

        (
            "System",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),

    )

    def colored_status(self, obj):

        colors = {
            "new": "#ef4444",          # Red
            "in_progress": "#f59e0b",  # Orange
            "answered": "#22c55e",     # Green
            "closed": "#6b7280",       # Gray
        }

        return format_html(
            '<strong style="color:{};">{}</strong>',
            colors.get(obj.status, "#000000"),
            obj.get_status_display(),
        )

    colored_status.short_description = "Status"

    def save_model(self, request, obj, form, change):
        """
        Automatically assign the admin who replied,
        set the reply timestamp,
        and mark the message as answered.
        """

        if obj.admin_reply:

            if obj.answered_by is None:
                obj.answered_by = request.user

            if obj.answered_at is None:
                obj.answered_at = timezone.now()

            if obj.status == ContactMessage.Status.NEW:
                obj.status = ContactMessage.Status.ANSWERED

        super().save_model(request, obj, form, change)