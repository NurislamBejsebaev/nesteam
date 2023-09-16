from rest_framework.viewsets import ModelViewSet
from .models import GameCollection
from .serializers import CollectionSerializer
from .filters import GamecollectionFilter
from rest_framework import filters



class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = GamecollectionFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


