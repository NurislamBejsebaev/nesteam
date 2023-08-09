from rest_framework import serializers
from .models import *


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

