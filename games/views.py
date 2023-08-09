from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import GameSerializers, StudioSerializer


class GameList(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class StudioList(generics.ListAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
