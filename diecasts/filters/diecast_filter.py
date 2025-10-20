import django_filters
from ..models.Diecast import Diecast

class DiecastFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name__name', lookup_expr='icontains')
    brand = django_filters.CharFilter(field_name='brand__name', lookup_expr='iexact')
    car_brand = django_filters.CharFilter(field_name='car_brand__name', lookup_expr='iexact')
    car_model = django_filters.CharFilter(field_name='car_model__name', lookup_expr='icontains')
    
    class Meta:
        model = Diecast
        
        fields = ['brand', 'name', 'car_brand', 'car_model']