from django.urls import path

from .views import (
    AdminConfirmCashPaymentView,
    CashPaymentView,
    MyPaymentsView,
    AdminPaymentListView,
    AdminPaymentDetailView,
)


urlpatterns = [

    path(
        "<int:booking_id>/cash/",
        CashPaymentView.as_view(),
        name="cash-payment"
    ),

    path(
        "my/",
        MyPaymentsView.as_view(),
        name="my-payments"
    ),

    path(
        "admin/",
        AdminPaymentListView.as_view(),
        name="admin-payments"
    ),

    path(
        "admin/<int:pk>/",
        AdminPaymentDetailView.as_view(),
        name="admin-payment-detail"
    ),
    path(
    "admin/<int:pk>/confirm-cash/",
    AdminConfirmCashPaymentView.as_view(),
    name="admin-confirm-cash-payment"
),
    

]