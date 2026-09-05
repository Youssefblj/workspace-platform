from django.db import models
from apps.users.models import User
from apps.offices.models import Office


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites'
    )

    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'office']
        ordering = ["-created_at"]


    def __str__(self):
        return f"{self.user.username} - {self.office.title}"