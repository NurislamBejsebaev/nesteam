from rest_framework import serializers
from .models import *


# class GameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = '__all__'
#
#
# class GameSerializersCreate(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = '__all__'


# class GameSerializersUpdate(serializers.ModelSerializer):
# #     class Meta:
# #         model = Game
# #         fields = '__all__'


class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class StudioSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

