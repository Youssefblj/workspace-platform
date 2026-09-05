from django.urls import path
from .views import (AdminBookingDetailView, AdminBookingStatusView, BookingCreateView,
BookingCreateView, MyBookingsView,AdminBookingListView, AdminBookingDeleteView, OfficeReservedDatesView,    AdminCreateBookingView)

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('my/', MyBookingsView.as_view(), name='my-bookings'),
    path('admin/', AdminBookingListView.as_view(), name='admin-bookings'),
    path("admin/<int:pk>/",AdminBookingDetailView.as_view(),name="admin-booking-detail"),
    path("admin/<int:pk>/status/",AdminBookingStatusView.as_view(),name="admin-booking-status"),
    path("admin/<int:pk>/delete/",AdminBookingDeleteView.as_view(),name="admin-booking-delete"),
    path("office/<int:office_id>/reserved-dates/",OfficeReservedDatesView.as_view(),name="office-reserved-dates"),
    path("admin/create/",AdminCreateBookingView.as_view(),name="admin-booking-create"),
]
