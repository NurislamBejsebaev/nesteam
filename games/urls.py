from django.urls import path
from games.views import *


urlpatterns = [
    # path('list/', GameList.as_view(), name='games-list'),
    # path('create/', GameCreate.as_view(), name='games-create'),
    # path('update/<int:pk>/', GameUpdate.as_view(), name='games-update'),
    # path('detail/<int:pk>/', GameDetail.as_view(), name='games-detail'),
    path('list/', StudioList.as_view(), name='studio-list'),
    path('create/', StudioCreate.as_view(), name='studio-create'),
]

