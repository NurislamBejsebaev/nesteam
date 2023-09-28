from .serializers import *
from .models import *
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class GamesView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CreateGamesAPIView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class StudiosViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    permission_classes = [IsAuthenticated]


