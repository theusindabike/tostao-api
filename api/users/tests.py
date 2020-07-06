from rest_framework.test import APITestCase
from rest_framework import status

from api.users.models import User


class UserAPITest(APITestCase):
    def test_get(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 0)
