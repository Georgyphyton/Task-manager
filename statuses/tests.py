from django.test import TestCase, Client
from django.urls import reverse_lazy
from users.models import CustomUser
from statuses.models import Statuses
from statuses.forms import CreateStatusForm
import os
import json


class TestStatuses(TestCase):
    fixtures = ['statuses.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.login_url = reverse_lazy('login')
        self.statuses_url = reverse_lazy('statuses')
        self.create_status_url = reverse_lazy('create_status')
        self.status1 = Statuses.objects.get(pk=1)
        self.status2 = Statuses.objects.get(pk=2)
        self.user = CustomUser.objects.get(pk=1)
        self.update_pk1_url = reverse_lazy('update_status', kwargs={'pk': 1})
        self.delete_pk1_url = reverse_lazy('delete_status', kwargs={'pk': 1})
        self.delete_pk2_url = reverse_lazy('delete_status', kwargs={'pk': 2})
        with open(os.path.join('fixtures', 'test_status.json')) as file:
            self.test_status = json.load(file)
        return super().setUp()

    def test_open_statuses(self):
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.statuses_url)
        self.assertEqual(response.status_code, 200)

    def test_get_create_status(self):
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 200)

    def test_post_create_status(self):
        self.client.force_login(self.user)
        response = self.client.post(self.create_status_url, self.test_status)
        self.assertRedirects(response, self.statuses_url, 302)
        self.status = Statuses.objects.get(pk=3)
        self.assertEqual(self.status.name, self.test_status.get('name'))

    def test_form_with_data(self):
        status_from = CreateStatusForm(self.test_status)
        self.assertTrue(status_from.is_valid)
        self.assertEqual(len(status_from.errors), 0)

    def test_form_with_empty_data(self):
        status_from = CreateStatusForm({})
        self.assertTrue(status_from.is_valid)
        self.assertEqual(len(status_from.errors), 1)

    def test_get_update_page(self):
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.update_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_update_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.update_pk1_url, self.test_status)
        self.assertEqual(response.status_code, 302)
        self.status = Statuses.objects.get(pk=1)
        self.assertEqual(self.status.name, self.test_status.get('name'))

    def test_get_delete_page(self):
        response = self.client.get(self.create_status_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.delete_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.delete_pk1_url)
        self.assertRedirects(response, self.statuses_url, 302)
        self.assertEqual(Statuses.objects.count(), 1)
        with self.assertRaises(Statuses.DoesNotExist):
            Statuses.objects.get(pk=1)
