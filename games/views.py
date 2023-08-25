from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.viewsets import *


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer


class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializers(data=data)
        if serializer.is_valid():
            game = Game()
            game.name = serializer.validated_data['name']
            game.year = serializer.validated_data['year']
            game.genre = serializer.validated_data['genre']
            game.studio = serializer.validated_data['studio']
            game.save()
            serializer = GameSerializers(instance=game)
            return HttpResponse(serializer.data, status=201)
        else:
            errors = serializer.error_messages
            response = {
                'message': 'данные не валидные',
                'errors': errors
            }
            return Response(
                data=response,
                status=400
                     )





