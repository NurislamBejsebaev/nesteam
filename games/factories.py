import factory
from .models import Game, Genre


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(lambda n: f'Game {n}')
    year = 2023


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(lambda n: f'Genre {n}')

