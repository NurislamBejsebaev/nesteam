from django.urls import path
from games.views import *


urlpatterns = [
    path('games/<int:pk>/', GamesView.as_view(), name='games'),
    path('list-create/', CreateGamesAPIView.as_view(), name='games'),
    path('studios/', StudiosListAPIView.as_view(), name='games'),
]

