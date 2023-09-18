from django.urls import path, include
from usersapp.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api-users', UserViewSet)

urlpatterns = [
    path('list/', UsersList.as_view(), name='user-list'),
    path('detail/<int:pk>/', UsersDetail.as_view(), name='user-detail'),
    path('user-router/', include(router.urls)),
    path('players/', PlayerListAPIView.as_view(), name='players'),
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authorization/', AuthorizationAPIView.as_view(), name='authorization'),
    path('auth-drf/', AuthDRFAPIView.as_view(), name='auth-drf'),
]
