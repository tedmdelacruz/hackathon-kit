from django.test import TestCase
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status

from web import views
from api.util import d


class AuthTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_registered_user_can_login(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'jdoe@test.com',
            'username': 'jdoe',
            'password': 'somepassword',
        }
        response = self.client.post('/register', data=data)
        new_user = User.objects.get(username='jdoe')

        self.assertIsInstance(new_user, User)
        self.assertRedirects(response, '/login')

        login_data = {
            'username': 'jdoe',
            'password': 'badpassword',
        }
        response = self.client.post('/login', data=login_data)
        self.assertRedirects(response, '/login')

        login_data = {
            'username': 'jdoe',
            'password': 'somepassword',
        }
        response = self.client.post('/login', data=login_data)
        self.assertRedirects(response, '/')

    def test_register_failure(self):
        pass

    def test_login_success(self):
        pass

    def test_login_invalid(self):
        pass
