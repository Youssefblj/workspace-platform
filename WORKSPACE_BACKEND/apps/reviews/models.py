from django.db import models
from apps.users.models import User
from apps.offices.models import Office


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    rating = models.IntegerField(choices=RATING_CHOICES)

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'office']

    def __str__(self):
        return f"{self.user.username} - {self.office.title}"