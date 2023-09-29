from django.urls import path, include
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'studios', StudiosViewSet)

urlpatterns = [
    path('games/<int:pk>/', GamesView.as_view(), name='games'),
    path('list-create/', CreateGamesAPIView.as_view(), name='games-create'),
    path('games-search/', GamesSearchView.as_view(), name='games-search'),
    path('', include(router.urls)),
]

