import django_filters
from .models import Office


class OfficeFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte'
    )

    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte'
    )

    class Meta:
        model = Office
        fields = {
            'workspace_type': ['exact'],
            'city': ['exact'],
            'wifi': ['exact'],
            'parking': ['exact'],
            'meeting_room': ['exact'],
            'air_conditioning': ['exact'],
            'available': ['exact'],
            'rent_type': ['exact'],
        }