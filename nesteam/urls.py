from django.contrib import admin
from django.urls import path
from games.views import *
from usersapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', GameList.as_view(), name='games-list'),
    path('studios/', StudioList.as_view(), name='studio-list'),
    path('users/', UsersList.as_view(), name='users-list'),
]
