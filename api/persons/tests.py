from rest_framework.test import APITestCase
from rest_framework import status

from api.persons.models import Person


class UserAPITest(APITestCase):
    def test_get(self):
        response = self.client.get('/api/persons/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.count(), 0)

    def test_post(self):
        response = self.client.post('/api/persons/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
