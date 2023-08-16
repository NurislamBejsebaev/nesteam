from django.contrib import admin
from django.urls import path, include
from games.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('games.urls')),
    path('studios/', include('games.urls')),
    path('users/', include('usersapp.urls')),
    path('', include(router.urls)),
]
