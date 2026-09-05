from django.urls import path
from .views import (AdminNotificationDeleteView, AdminNotificationDetailView, AdminNotificationListView, AdminSendNotificationView, NotificationListView, NotificationReadView, 
                    UnreadNotificationCountView, MarkAllNotificationsReadView)

urlpatterns = [
    path('', NotificationListView.as_view()),
    path('read/<int:pk>/', NotificationReadView.as_view()),
    path('unread-count/', UnreadNotificationCountView.as_view()),
    path('mark-all-read/', MarkAllNotificationsReadView.as_view()),
    path("admin/",AdminNotificationListView.as_view()),
    path("admin/<int:pk>/",AdminNotificationDetailView.as_view()),
    path("admin/<int:pk>/delete/",AdminNotificationDeleteView.as_view()),
    path("admin/send/",AdminSendNotificationView.as_view()),
]