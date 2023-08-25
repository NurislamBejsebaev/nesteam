from django.test import TestCase
from rest_framework.test import APITestCase
from .models import *


class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        Genre(
            name='test1 genre name',
            description='test1 genre description'
        ).save()
        Studio(
            name='test1 studio name',
            workers_count=100,
            games_count=50
        ).save()
        data = {
            "name": "Game test1",
            "year": 2024,
            "genre": 1,
            "studio": 1
            }
        response = self.client.post('/games/create/', data=data)
        self.assertEqual(response.status_code, 201)

        game = Game.objects.last()
        self.assertEqual(game.name, data['name'])
        self.assertEqual(game.year, data['year'])
        self.assertEqual(game.genre.id, data['genre'])
        self.assertEqual(game.studio.id, data['studio'])

    def test_create_game_with_wrong_data_should_fail(self):
        response = self.client.post('/games/create/', data={"test1": 'lorem'})
        self.assertEqual(response.status_code, 400)

    # def test_create_game_via_get_request_should_return_405(self):
    #     data = {
    #         "name": "Wrong form",
    #         "year": 2024,
    #         "genre": 1,
    #         "studio": 1
    #     }
    #     response = self.client.get('/games/create/', data=data)
    #     self.assertEqual(response.status_code, 405)
    #     games_exists = Game.objects.filter(name="Wrong form").exists()
    #     self.assertFalse(games_exists)

