from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

from app.web import views


class AuthTest(TestCase):
    created_users = []

    def setUp(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'jdoe@test.com',
            'username': 'jdoe',
            'password': 'somepassword',
        }
        self.existing_user = User.objects.create_user(**data)

    def tearDown(self):
        self.existing_user.delete()
        for user in self.created_users:
            user.delete()

    def test_authenticate(self):
        user = auth.authenticate(username='jdoe', password='somepassword')
        self.assertEquals(self.existing_user, user)

    def test_user_can_register(self):
        data = {
            'first_name': 'Juan',
            'last_name': 'dela Cruz',
            'email': 'jdelacruz@test.com',
            'username': 'jdelacruz',
            'password': 'somepassword',
        }
        response = self.client.post('/register', data=data)
        new_user = User.objects.get(username='jdelacruz')
        self.created_users.append(new_user)

        self.assertIsInstance(new_user, User)
        self.assertRedirects(response, '/login')

    def test_registered_user_can_login(self):
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
