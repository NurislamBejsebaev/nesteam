from rest_framework import generics
from .serializers import *
from rest_framework.viewsets import *
from django.contrib.auth.models import User


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializers


class UsersDetail(generics.RetrieveAPIView):
    serializer_class = UsersListSerializers
    queryset = User.objects.all()


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UsersSerializers


