from django.urls import path
from .views import (AdminToggleUserActiveView, AdminUserDeleteView, AdminUserDetailView,
                    AdminUsersListView, ChangePasswordView, RegisterView, ProfileView,
                    ProfileUpdateView,ForgotPasswordView, ResetPasswordView, AdminUserUpdateView,DeleteMyAccountView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path("delete-account/",DeleteMyAccountView.as_view(),name="delete-account"),
    path('admin/users/',AdminUsersListView.as_view(),name='admin-users-list'),
    path("admin/users/<int:id>/",AdminUserDetailView.as_view(),name="admin-user-detail"),
    path("admin/users/<int:id>/update/",AdminUserUpdateView.as_view(),name="admin-user-update"),
    path("admin/users/<int:id>/delete/",AdminUserDeleteView.as_view(),name="admin-user-delete"),
    path("admin/users/<int:id>/toggle-active/",AdminToggleUserActiveView.as_view(),name="admin-user-toggle-active")
    ]