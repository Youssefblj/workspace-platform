from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.bookings.models import Booking
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import ReviewAdminPermission


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        office_id = self.kwargs['office_id']
        return Review.objects.filter(office_id=office_id)


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        office = serializer.validated_data['office']

        has_booking = Booking.objects.filter(
            user=self.request.user,
            office=office
        ).exists()

        if not has_booking:
            from rest_framework.exceptions import ValidationError
            raise ValidationError(
                "You must book this office before reviewing it."
            )

        serializer.save(user=self.request.user)
        
class AdminReviewListView(generics.ListAPIView):

    queryset = Review.objects.select_related(
        "user",
        "office"
    )

    serializer_class = ReviewSerializer

    permission_classes = [ReviewAdminPermission]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = [
        "rating",
        "office",
    ]

    search_fields = [
        "comment",
        "user__username",
        "office__title",
    ]

    ordering_fields = [
        "created_at",
        "rating",
    ]
    
class AdminReviewDetailView(generics.RetrieveAPIView):

    queryset = Review.objects.select_related(
        "user",
        "office"
    )

    serializer_class = ReviewSerializer

    permission_classes = [ReviewAdminPermission]
    
    
class AdminReviewDeleteView(generics.DestroyAPIView):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    permission_classes = [ReviewAdminPermission]