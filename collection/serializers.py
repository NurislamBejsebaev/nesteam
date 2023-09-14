from .models import GameCollection
from rest_framework.serializers import ModelSerializer


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = GameCollection
        fields = '__all__'

