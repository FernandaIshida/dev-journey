from django.contrib.auth.models import User
from rest_framework.test import APITestCase 
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Students-list')

    def test_authentication_user(self):
        """
        Test if the user is authenticated correctly.
        """
        user = authenticate(username='admin', password='admin')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_authentication_user_wrong_password(self):
        """
        Test if the user is not authenticated with wrong password.
        """
        user = authenticate(username='admin', password='wrongpassword')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_authentication_user_wrong_username(self):
        """
        Test if the user is not authenticated with wrong username.
        """
        user = authenticate(username='wrongusername', password='admin')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_request_authorized(self):
        """"
        Test that verifies an authorized GET request.
        """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_request_unauthorized(self):
        """"
        Test that verifies an unauthorized GET request.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
