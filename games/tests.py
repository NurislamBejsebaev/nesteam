from rest_framework.test import APITestCase
from .factories import *


class GamesTest(APITestCase):
    def setUp(self):
        self.game_1 = GameFactory(year=2024)
        self.game_2 = GameFactory(year=2024)
        self.genre = GenreFactory()

    def test_get_list_of_games(self):
        response = self.client.get('/games/list-create/')
        self.assertEqual(response.status_code, 200)



    def test_get_one_game(self):
        response = self.client.get(f'/games/games/{self.game_1.pk}/')
        self.assertEqual(response.status_code, 200)



    def test_get_genre(self):
        response = self.client.get(f'/genre/{self.genre.pk}/')
        self.assertEqual(response.status_code, 200)
