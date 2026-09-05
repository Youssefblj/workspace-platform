from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .serializers import OfficeSerializer, OfficeImageSerializer, AdminOfficeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OfficeFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Office, OfficeImage
from rest_framework import status



class OfficeListView(generics.ListAPIView):

    queryset = Office.objects.filter(
        is_active=True
    )

    serializer_class = OfficeSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]

    filterset_class = OfficeFilter

    search_fields = [
        'title',
        'city',
        'description'
    ]
class OfficeDetailView(generics.RetrieveAPIView):
    queryset = Office.objects.filter(
        is_active=True
    )
    serializer_class = OfficeSerializer


class OfficeCreateView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [IsAdminUser]


class OfficeUpdateView(generics.UpdateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [IsAdminUser]


class OfficeDeleteView(generics.DestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [IsAdminUser]
    
class OfficeImageUploadView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, office_id):
        try:
            office = Office.objects.get(id=office_id)
        except Office.DoesNotExist:
            return Response(
                {"error": "Office not found"},
                status=404
            )

        image = request.FILES.get('image')

        if not image:
            return Response(
                {"error": "No image uploaded"},
                status=400
            )

        office_image = OfficeImage.objects.create(
            office=office,
            image=image
        )

        serializer = OfficeImageSerializer(office_image)

        return Response({
            "message": "Image uploaded successfully",
            "image": serializer.data
        }, status=201)


class AdminOfficeListView(generics.ListAPIView):

    queryset = Office.objects.all().order_by("-created_at")

    serializer_class = AdminOfficeSerializer

    permission_classes = [IsAdminUser]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = OfficeFilter

    search_fields = [
        "title",
        "city",
        "description",
        "address",
    ]

    ordering_fields = [
        "price",
        "created_at",
        "capacity",
    ]

class AdminOfficeDetailView(generics.RetrieveAPIView):

    queryset = Office.objects.all()

    serializer_class = AdminOfficeSerializer

    permission_classes = [IsAdminUser]

    lookup_field = "pk"
    
class AdminOfficeUpdateView(generics.UpdateAPIView):

    queryset = Office.objects.all()

    serializer_class = AdminOfficeSerializer

    permission_classes = [IsAdminUser]

    lookup_field = "pk"
    
class AdminOfficeDeleteView(generics.DestroyAPIView):

    queryset = Office.objects.all()

    permission_classes = [IsAdminUser]

    lookup_field = "pk"
    
class AdminToggleOfficeAvailabilityView(APIView):

    permission_classes = [IsAdminUser]

    def patch(self, request, pk):

        office = Office.objects.get(pk=pk)

        office.available = not office.available

        office.save()

        return Response({
            "message": "Availability updated successfully",
            "available": office.available
        })
        
        
class AdminOfficeStatisticsView(APIView):

    permission_classes = [IsAdminUser]

    def get(self, request):

        data = {
            "total_offices": Office.objects.count(),

            "available": Office.objects.filter(
                available=True
            ).count(),

            "unavailable": Office.objects.filter(
                available=False
            ).count(),

            "office": Office.objects.filter(
                workspace_type="office"
            ).count(),

            "coworking": Office.objects.filter(
                workspace_type="coworking"
            ).count(),

            "meeting": Office.objects.filter(
                workspace_type="meeting"
            ).count(),

            "virtual": Office.objects.filter(
                workspace_type="virtual"
            ).count(),
        }

        return Response(data)
    
class SetPrimaryOfficeImageView(APIView):

    permission_classes = [IsAdminUser]

    def patch(self, request, pk):

        try:

            image = OfficeImage.objects.get(pk=pk)

        except OfficeImage.DoesNotExist:

            return Response(
                {"detail": "Image not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        OfficeImage.objects.filter(
            office=image.office
        ).update(
            is_primary=False
        )

        image.is_primary = True

        image.save()

        return Response({

            "message": "Primary image updated successfully."

        })
        


class OfficeImageDeleteView(generics.DestroyAPIView):

    queryset = OfficeImage.objects.all()

    serializer_class = OfficeImageSerializer

    permission_classes = [IsAdminUser]
    
class AdminToggleOfficeActiveView(APIView):

    permission_classes = [
        IsAdminUser
    ]

    def patch(self, request, pk):

        try:
            office = Office.objects.get(
                pk=pk
            )

        except Office.DoesNotExist:
            return Response(
                {
                    "error":
                        "Office not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )


        office.is_active = (
            not office.is_active
        )

        office.save(
            update_fields=[
                "is_active"
            ]
        )


        return Response(
            {
                "message": (
                    "Office activated successfully."
                    if office.is_active
                    else
                    "Office deactivated successfully."
                ),

                "is_active":
                    office.is_active
            },
            status=status.HTTP_200_OK
        )