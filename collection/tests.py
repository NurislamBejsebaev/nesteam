import json
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .factories import CollectionFactory
from usersapp.factories import UserFactory
from .models import GameCollection


class CollectionsTest(APITestCase):
    def setUp(self):
        self.col_1 = CollectionFactory()
        self.col_2 = CollectionFactory()
        self.col_3 = CollectionFactory()
        self.client = APIClient()

    def test_get_list_of_3_collections(self):
        user = UserFactory()
        token, _ = Token.objects.get_or_create(user=user)
        self.col_1 = CollectionFactory(name='Test collection 7')
        self.col_2 = CollectionFactory(name='Test collection 8')
        self.col_3 = CollectionFactory(name='Test collection 9')
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = self.client.get('/collections/')
        self.assertEqual(response.status_code, 200)
        collections = response.data['results']
        self.assertEqual(self.col_1.name, collections[0]["name"])
        self.assertEqual(self.col_2.name, collections[1]["name"])
        self.assertEqual(self.col_3.name, collections[2]["name"])

    def test_get_one_collection(self):
        user = UserFactory()
        token, _ = Token.objects.get_or_create(user=user)

        # Создаем коллекцию
        self.col_1 = CollectionFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = self.client.get(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data["name"])

    def test_create_collection(self):
        user = UserFactory()
        token, _ = Token.objects.get_or_create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        collection_data = {
            'name': 'New collection',
            'likes': [1],
            'author': 1
        }
        response = self.client.post('/collections/', json.dumps(collection_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_collection(self):
        user = UserFactory(pk=1)  # Указываем первичный ключ 1
        token, _ = Token.objects.get_or_create(user=user)
        self.col_1 = CollectionFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        updated_name = 'New Collection Name'
        updated_data = {
            'name': updated_name,
            'likes': [1],  # Используем корректные первичные ключи лайков
            'author': user.pk  # Используем корректный первичный ключ автора
        }
        response = self.client.put(f'/collections/{self.col_1.pk}/', updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_name, response.data["name"])


    def test_delete_collection(self):
        user = UserFactory()
        token, _ = Token.objects.get_or_create(user=user)
        self.col_1 = CollectionFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = self.client.delete(f'/collections/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(GameCollection.objects.count(), 3)













