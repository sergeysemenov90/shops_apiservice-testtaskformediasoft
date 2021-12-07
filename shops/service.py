from django_filters import rest_framework as filters
from .models import Shop


class ShopsFilter(filters.FilterSet):
    city = filters.BaseInFilter(field_name='city')
    street = filters.BaseInFilter(field_name='street')

    class Meta:
        model = Shop
        fields = ['city', 'street',]