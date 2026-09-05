from django.urls import path

from .views import (
    PublicSiteSettingsView,
    AdminSiteSettingsView,
)


urlpatterns = [

    path(
        "",
        PublicSiteSettingsView.as_view(),
        name="site-settings"
    ),

    path(
        "admin/",
        AdminSiteSettingsView.as_view(),
        name="admin-site-settings"
    ),

]