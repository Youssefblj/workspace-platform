from django.db import models


class SiteSettings(models.Model):
    website_name = models.CharField(
        max_length=100,
        default="WorkSpace"
    )

    website_url = models.URLField(
        blank=True
    )

    contact_email = models.EmailField(
        blank=True
    )

    contact_phone = models.CharField(
        max_length=20,
        blank=True
    )

    whatsapp_number = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    facebook_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )
    twitter_url = models.URLField(
    blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.website_name