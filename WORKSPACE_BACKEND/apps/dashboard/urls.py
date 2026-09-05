from django.urls import path
from .views import DashboardView,PublicStatsView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path(
        "public-stats/",
        PublicStatsView.as_view(),
        name="public-stats"
    ),
    
]