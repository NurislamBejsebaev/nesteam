from django.shortcuts import render
from rest_framework import generics
from .serializers import UsersSerializers
from django.contrib.auth.models import User


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializers


