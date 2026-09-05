"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/bookings/', include('apps.bookings.urls')),
    path('api/offices/', include('apps.offices.urls')),
    path('api/payments/', include('apps.payments.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/favorites/', include('apps.favorites.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
    path ('api/contact/', include('apps.contact.urls')),
    path("api/site-settings/",include("apps.site_settings.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
    'api/docs/',
    SpectacularSwaggerView.as_view(url_name='schema'),
    name='swagger-ui'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
