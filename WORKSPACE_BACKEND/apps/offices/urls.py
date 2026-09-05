from django.urls import path
from .views import (
    AdminOfficeDeleteView,
    AdminOfficeDetailView,
    AdminOfficeListView,
    AdminOfficeStatisticsView,
    AdminOfficeStatisticsView,
    AdminOfficeUpdateView,
    AdminToggleOfficeAvailabilityView,
    OfficeImageDeleteView,
    OfficeListView,
    OfficeDetailView,
    OfficeCreateView,
    OfficeUpdateView,
    OfficeDeleteView,
    OfficeImageUploadView,
    SetPrimaryOfficeImageView,
    AdminToggleOfficeActiveView
)

urlpatterns = [
    path('', OfficeListView.as_view(), name='office-list'),
    path('<int:pk>/', OfficeDetailView.as_view(), name='office-detail'),
    path('create/', OfficeCreateView.as_view(), name='office-create'),
    path('<int:pk>/update/', OfficeUpdateView.as_view(), name='office-update'),
    path('<int:pk>/delete/', OfficeDeleteView.as_view(), name='office-delete'),
    path('<int:office_id>/upload-image/', OfficeImageUploadView.as_view(), name='office-image-upload'),
    path("images/<int:pk>/set-primary/",SetPrimaryOfficeImageView.as_view(),name="office-image-primary"),
    path("images/<int:pk>/delete/",OfficeImageDeleteView.as_view(),name="office-image-delete"),
    
    path("admin/",AdminOfficeListView.as_view(),name="admin-office-list"),
    path("admin/<int:pk>/",AdminOfficeDetailView.as_view(),name="admin-office-detail"),
    path("admin/<int:pk>/update/",AdminOfficeUpdateView.as_view(),name="admin-office-update"),
    path("admin/<int:pk>/delete/",AdminOfficeDeleteView.as_view(),name="admin-office-delete"),
    path("admin/<int:pk>/toggle-availability/",AdminToggleOfficeAvailabilityView.as_view(),name="admin-office-toggle"),
    path("admin/statistics/",AdminOfficeStatisticsView.as_view(),name="admin-office-statistics"),
    path("admin/<int:pk>/toggle-active/",AdminToggleOfficeActiveView.as_view(),name="admin-office-toggle-active"
),
]