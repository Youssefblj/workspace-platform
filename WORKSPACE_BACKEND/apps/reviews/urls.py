from django.urls import path
from .views import AdminReviewDeleteView, AdminReviewDetailView, AdminReviewListView, ReviewListView, ReviewCreateView

urlpatterns = [
path('office/<int:office_id>/', ReviewListView.as_view(), name='review-list'),
path('create/', ReviewCreateView.as_view(), name='review-create'),
path("admin/",AdminReviewListView.as_view(),name="admin-review-list"),
path("admin/<int:pk>/",AdminReviewDetailView.as_view(),name="admin-review-detail"),
path("admin/<int:pk>/delete/",AdminReviewDeleteView.as_view(),name="admin-review-delete"),
]