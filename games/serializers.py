from rest_framework import serializers
from .models import *


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'
