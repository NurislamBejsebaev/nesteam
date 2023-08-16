from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.viewsets import *


# class GameList(generics.ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers
#
#
# class GameCreate(generics.ListCreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializersCreate
#
#
# class GameUpdate(generics.RetrieveUpdateAPIView):
#     serializer_class = GameSerializers
#     queryset = Game.objects.all()
#
#
# class GameDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = GameSerializers
#     queryset = Game.objects.all()


class StudioList(generics.ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class StudioCreate(generics.ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializerCreate


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
