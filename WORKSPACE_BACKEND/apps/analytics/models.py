from django.db import models
from apps.users.models import User


class VisitorLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    page = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    visited_at = models.DateTimeField(auto_now_add=True)