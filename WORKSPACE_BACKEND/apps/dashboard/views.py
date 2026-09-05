from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from django.db.models import Sum
from django.utils import timezone

from apps.users.models import User
from apps.offices.models import Office
from apps.bookings.models import Booking
from apps.payments.models import Payment
from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework.permissions import AllowAny

from apps.reviews.models import Review

class DashboardView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        # =========================
        # Users Statistics
        # =========================

        total_users = User.objects.count()

        active_users = User.objects.filter(
            is_active=True
        ).count()

        inactive_users = User.objects.filter(
            is_active=False
        ).count()

        # =========================
        # Offices Statistics
        # =========================

        total_offices = Office.objects.count()

        available_offices = Office.objects.filter(
            available=True
        ).count()

        unavailable_offices = Office.objects.filter(
            available=False
        ).count()

        # =========================
        # Bookings Statistics
        # =========================

        total_bookings = Booking.objects.count()

        pending_bookings = Booking.objects.filter(
            status="pending"
        ).count()

        confirmed_bookings = Booking.objects.filter(
            status="confirmed"
        ).count()

        cancelled_bookings = Booking.objects.filter(
            status="cancelled"
        ).count()

        today = timezone.now().date()

        today_bookings = Booking.objects.filter(
            created_at__date=today
        ).count()

        # =========================
        # Revenue Statistics
        # =========================

        total_revenue = Payment.objects.filter(
            status="paid"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0

        today_revenue = Payment.objects.filter(
            status="paid",
            created_at__date=today
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0

        now = timezone.now()

        this_month_revenue = Payment.objects.filter(
            status="paid",
            created_at__year=now.year,
            created_at__month=now.month
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0

        # =========================
        # Recent Bookings
        # =========================

        recent_bookings = list(
            Booking.objects.select_related(
                "user",
                "office"
            )
            .order_by("-created_at")[:5]
            .values(
                "id",
                "user__username",
                "office__title",
                "office__city",
                "start_date",
                "end_date",
                "total_price",
                "status",
                "created_at",
            )
        )

        # =========================
        # Recent Payments
        # =========================

        recent_payments = list(
            Payment.objects.select_related(
                "user",
                "booking",
                "booking__office"
            )
            .order_by("-created_at")[:5]
            .values(
                "id",
                "user__username",
                "booking__office__title",
                "amount",
                "currency",
                "status",
                "created_at",
            )
        )

        # =========================
        # Response
        # =========================

        return Response({
            # Users
            "total_users": total_users,
            "active_users": active_users,
            "inactive_users": inactive_users,

            # Offices
            "total_offices": total_offices,
            "available_offices": available_offices,
            "unavailable_offices": unavailable_offices,

            # Bookings
            "total_bookings": total_bookings,
            "pending_bookings": pending_bookings,
            "confirmed_bookings": confirmed_bookings,
            "cancelled_bookings": cancelled_bookings,
            "today_bookings": today_bookings,

            # Revenue
            "total_revenue": total_revenue,
            "today_revenue": today_revenue,
            "this_month_revenue": this_month_revenue,

            # Recent Activity
            "recent_bookings": recent_bookings,
            "recent_payments": recent_payments,

        })
        
        


User = get_user_model()


class PublicStatsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        workspaces = Office.objects.count()

        members = User.objects.filter(
            is_active=True,
            is_staff=False,
            is_superuser=False
        ).count()

        bookings = Booking.objects.filter(
            status="confirmed"
        ).count()

        cities = (
            Office.objects
            .exclude(city__isnull=True)
            .exclude(city="")
            .values("city")
            .distinct()
            .count()
        )

        average_rating = (
            Review.objects.aggregate(
                average=Avg("rating")
            )["average"]
            or 0
        )

        total_reviews = Review.objects.count()

        positive_reviews = Review.objects.filter(
            rating__gte=4
        ).count()

        satisfaction = (
            round(
                positive_reviews / total_reviews * 100
            )
            if total_reviews > 0
            else 0
        )

        return Response({
            "workspaces": workspaces,
            "members": members,
            "bookings": bookings,
            "cities": cities,
            "average_rating": round(
                float(average_rating),
                1
            ),
            "satisfaction": satisfaction,
        })