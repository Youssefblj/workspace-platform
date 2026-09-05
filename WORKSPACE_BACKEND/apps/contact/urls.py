from django.urls import path

from .views import (
    ContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactReplyView,
    ContactUpdateView,
    ContactDeleteView,
    MyContactMessagesView,
    
)

urlpatterns = [
    path("", ContactListView.as_view(), name="contact-list"),
    path("<int:pk>/",ContactDetailView.as_view(),name="contact-detail"),
    path("create/", ContactCreateView.as_view(),name="contact-create"),
    path("<int:pk>/update/",ContactUpdateView.as_view(),name="contact-update"),
    path("<int:pk>/delete/",ContactDeleteView.as_view(),   name="contact-delete"),
    path("<int:pk>/reply/",ContactReplyView.as_view(),name="contact-reply"),
    path( "my/", MyContactMessagesView.as_view(), name="my-contact-messages" ),
]