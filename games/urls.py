from django.urls import path, include
from games.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api-studio', StudioViewSet)

urlpatterns = [
    path('create/', GameCreateAPIView.as_view(), name='games-create'),
    path('studio-router/', include(router.urls)),
]

