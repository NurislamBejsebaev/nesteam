from django_filters import rest_framework as filters
from .models import GameCollection


class GamecollectionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = GameCollection
        fields = ['name']

