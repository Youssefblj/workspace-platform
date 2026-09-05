from django.db import models

class Office(models.Model):
    WORKSPACE_TYPES = (
    ('office', 'Office'),
    ('coworking', 'Coworking Space'),
    ('meeting', 'Meeting Room'),
    ('virtual', 'Virtual Office'),
    )
    
    
    RENT_TYPE = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    )
    
    workspace_type = models.CharField(
    max_length=20,
    choices=WORKSPACE_TYPES,
    default='office'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    city = models.CharField(max_length=100)
    address = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    rent_type = models.CharField(max_length=20, choices=RENT_TYPE)

    capacity = models.IntegerField()
    available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    meeting_room = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class OfficeImage(models.Model):

    office = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="offices/"
    )

    is_primary = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.office.title} Image"