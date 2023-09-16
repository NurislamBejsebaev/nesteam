from rest_framework.viewsets import ModelViewSet
from .models import GameCollection
from .serializers import CollectionSerializer
from .filters import GamecollectionFilter



class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = GamecollectionFilter


