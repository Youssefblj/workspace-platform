from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class RegisterTests(APITestCase):

    def test_user_registration(self):
        data = {
            "username": "imad",
            "email": "imad@test.com",
            "phone": "0612345678",
            "password": "strongpass123"
        }

        response = self.client.post(
            '/api/register/',
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )