from .serializers import *
from .models import *
from rest_framework.viewsets import *
from rest_framework.generics import *


class GamesView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CreateGamesAPIView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class StudiosListAPIView(ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

