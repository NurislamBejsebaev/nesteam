from .serializers import *
from .models import *
from rest_framework.viewsets import *
from rest_framework.generics import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .mixins import HelloMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .paginations import GenrePagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

class GamesView(RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GenreViewSet(ModelViewSet):
    pagination_class = GenrePagination
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CreateGamesAPIView(LoginRequiredMixin, ListCreateAPIView, HelloMixin):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get(self, request, *args, **kwargs):
        self.say_hello()
        return super().get(request, *args, **kwargs)


class StudiosViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    permission_classes = [IsAuthenticated]


class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:
            key_word = request.GET['key_word']
        elif 'key_word' in request.data:
            key_word = request.data['key_word']
        else:
            return Response('no data', status=400)

        games = Game.objects.filter(
            Q(name__icontains=key_word) |
            Q(genre__name__icontains=key_word) |
            Q(studio__name__icontains=key_word)
        )

        serializer = GameSerializer(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)

