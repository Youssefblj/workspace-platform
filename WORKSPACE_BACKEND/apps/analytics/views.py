from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from apps.bookings.models import Booking
from django.db.models import Count, Avg, Sum
from django.db.models.functions import ExtractMonth
from apps.offices.models import Office
from apps.users.models import User
from apps.payments.models import Payment
from django.db.models import (
    Count,
    Avg,
    Sum
)

class AnalyticsView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        #
        # Dashboard Numbers
        #

        total_users = User.objects.count()

        total_offices = Office.objects.count()

        total_bookings = Booking.objects.count()

        total_revenue = (
            Payment.objects.filter(
                status="paid"
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0
        )

        #
        # Most booked office
        #

        most_booked = (
            Booking.objects.values(
                "office__title"
            )
            .annotate(
                total=Count("id")
            )
            .order_by("-total")
            .first()
        )

        #
        # Most popular city
        #

        popular_city = (
            Booking.objects.values(
                "office__city"
            )
            .annotate(
                total=Count("id")
            )
            .order_by("-total")
            .first()
        )

        #
        # Average booking price
        #

        average_price = (
            Booking.objects.aggregate(
                avg=Avg("total_price")
            )["avg"] or 0
        )

        #
        # Revenue per city
        #

        revenue_per_city = list(

            Payment.objects.filter(
            status="paid"
    )

            .values(
            "booking__office__city"
    )

            .annotate(
            revenue=Sum("amount")
    )

    .order_by("-revenue")
)

        #
        # Bookings per month
        #

        bookings_per_month = list(

            Booking.objects.annotate(
                month=ExtractMonth("created_at")
            )

            .values("month")

            .annotate(
                total=Count("id")
            )

            .order_by("month")

        )

        #
        # Revenue per month
        #

        revenue_per_month = list(

            Payment.objects.filter(
                status="paid"
            )

            .annotate(
                month=ExtractMonth("paid_at")
            )

            .values("month")

            .annotate(
                revenue=Sum("amount")
            )

            .order_by("month")

        )

        #
        # Booking Status
        #

        booking_status = {

            "pending":
            Booking.objects.filter(
                status="pending"
            ).count(),

            "confirmed":
            Booking.objects.filter(
                status="confirmed"
            ).count(),

            "cancelled":
            Booking.objects.filter(
                status="cancelled"
            ).count()

        }

        return Response({

            "dashboard": {

                "total_users": total_users,

                "total_offices": total_offices,

                "total_bookings": total_bookings,

                "total_revenue": total_revenue

            },

            "most_booked_office": most_booked,

            "most_popular_city": popular_city,

            "average_booking_price": average_price,

            "revenue_per_city": revenue_per_city,

            "bookings_per_month": bookings_per_month,

            "revenue_per_month": revenue_per_month,

            "booking_status": booking_status

        })