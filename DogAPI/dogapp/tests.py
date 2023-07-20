from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestPostToDogList(APITestCase):
    def setUp(self):
        self.dog_url = reverse('dog_list')
        self.dog_data = {
            "name": "Test Dog",
            "price": 1000,
            "breed": "Test Breed",
            "description": "Test Description",
        }
        return super().setUp()

    def test_for_creating_dog(self):
        response = self.client.post(self.dog_url, self.dog_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TestGetToDogList(APITestCase):
    def setUp(self):
        self.dog_url = reverse('dog_list')
        return super().setUp()

    def test_for_getting_dogs(self):
        response = self.client.get(self.dog_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestGetToDogDetails(APITestCase):
    def setUp(self):
        self.dog_data = {
            "name": "Test Dog",
            "price": 1000,
            "breed": "Test Breed",
            "description": "Test Description",
        }
        self.response = self.client.post(reverse('dog_list'), self.dog_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dog_url = reverse('dog_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_for_getting_dogDetails(self):
        response = self.client.get(self.dog_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPutToDogDetails(APITestCase):
    def setUp(self):
        self.dog_data = {
            "name": "Test Dog",
            "price": 1000,
            "breed": "Test Breed",
            "description": "Test Description",
        }
        self.response = self.client.post(reverse('dog_list'), self.dog_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dog_url = reverse('dog_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_for_putting_dog(self):
        self.dog_data = {
            "name": "Test Dog - Updated",
            "price": 1000,
            "breed": "Test Breed - Updated",
            "description": "Test Description - Updated",
        }
        response = self.client.put(self.dog_url, self.dog_data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

class TestDeleteToDogDetails(APITestCase):
    def setUp(self):
        self.dog_data = {
            "name": "Test Dog",
            "price": 1000,
            "breed": "Test Breed",
            "description": "Test Description",
        }
        self.response = self.client.post(reverse('dog_list'), self.dog_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dog_url = reverse('dog_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_for_deleting_dog(self):
        response = self.client.delete(self.dog_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)