from django.test import TestCase
from django.urls import reverse_lazy
from users.models import CustomUser
from users.forms import CreateUserForm
import os
import json


class TestUsers(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.register_url = reverse_lazy('create_user')
        self.login_url = reverse_lazy('login')
        self.users_url = reverse_lazy('users')
        self.user1 = CustomUser.objects.get(pk=1)
        self.user2 = CustomUser.objects.get(pk=2)
        self.update_pk1_url = reverse_lazy('update_user', kwargs={'pk': 1})
        self.delete_pk1_url = reverse_lazy('delete_user', kwargs={'pk': 1})
        self.delete_pk2_url = reverse_lazy('delete_user', kwargs={'pk': 2})
        with open(os.path.join('fixtures', 'test_user.json')) as user:
            self.test_user = json.load(user)
        return super().setUp()

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(self.register_url, self.test_user)
        self.assertRedirects(response, self.login_url, 302)
        self.user = CustomUser.objects.get(pk=3)
        self.assertEqual(self.user.username, self.test_user.get('username'))
        self.assertEqual(self.user.first_name,
                         self.test_user.get('first_name'))
        self.assertEqual(self.user.last_name, self.test_user.get('last_name'))

    def test_form_with_data(self):
        user_from = CreateUserForm(self.test_user)
        self.assertTrue(user_from.is_valid)
        self.assertEqual(len(user_from.errors), 0)

    def test_form_with_empty_data(self):
        user_from = CreateUserForm({})
        self.assertTrue(user_from.is_valid)
        self.assertEqual(len(user_from.errors), 3)

    def test_update_page(self):
        response = self.client.get(self.update_pk1_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(self.update_pk1_url, self.test_user)
        self.user = CustomUser.objects.get(pk=1)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.username, self.test_user.get('username'))
        self.assertEqual(self.user.first_name,
                         self.test_user.get('first_name'))
        self.assertEqual(self.user.last_name, self.test_user.get('last_name'))

    def test_delete_page(self):
        response = self.client.get(self.delete_pk1_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(self.delete_pk1_url)
        self.assertRedirects(response, self.users_url, 302)
        self.assertEqual(CustomUser.objects.count(), 1)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(pk=1)

