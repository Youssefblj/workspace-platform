# apps/favorites/urls.py

from django.urls import path

from .views import (
    FavoriteListView,
    FavoriteCreateView,
    FavoriteDeleteView
)


urlpatterns = [
    path(
        "",
        FavoriteListView.as_view(),
        name="favorite-list"
    ),

    path(
        "create/",
        FavoriteCreateView.as_view(),
        name="favorite-create"
    ),

    path(
        "delete/<int:pk>/",
        FavoriteDeleteView.as_view(),
        name="favorite-delete"
    ),
]