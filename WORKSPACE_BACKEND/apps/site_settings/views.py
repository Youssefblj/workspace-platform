from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import SiteSettings
from .serializers import SiteSettingsSerializer


def get_site_settings():
    settings, created = SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            "website_name": "WorkSpace"
        }
    )

    return settings


class PublicSiteSettingsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        settings = get_site_settings()

        serializer = SiteSettingsSerializer(
            settings,
            context={
                "request": request
            }
        )

        return Response(
            serializer.data
        )


class AdminSiteSettingsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):

        settings = get_site_settings()

        serializer = SiteSettingsSerializer(
            settings,
            context={
                "request": request
            }
        )

        return Response(
            serializer.data
        )

    def patch(self, request):

        settings = get_site_settings()

        serializer = SiteSettingsSerializer(
            settings,
            data=request.data,
            partial=True,
            context={
                "request": request
            }
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )

    def put(self, request):

        settings = get_site_settings()

        serializer = SiteSettingsSerializer(
            settings,
            data=request.data,
            context={
                "request": request
            }
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )