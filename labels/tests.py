from django.test import TestCase, Client
from django.urls import reverse_lazy
from users.models import CustomUser
from labels.models import Labels
from labels.forms import CreateLabelForm
from django.contrib.messages import get_messages
import os
import json


class TestLabels(TestCase):
    fixtures = ['labels.json', 'users.json', 'statuses.json', 'tasks.json']

    def setUp(self):
        self.client = Client()
        self.login_url = reverse_lazy('login')
        self.labels_url = reverse_lazy('labels')
        self.create_label_url = reverse_lazy('create_label')
        self.label1 = Labels.objects.get(pk=1)
        self.label2 = Labels.objects.get(pk=2)
        self.user = CustomUser.objects.get(pk=1)
        self.update_pk1_url = reverse_lazy('update_label', kwargs={'pk': 1})
        self.delete_pk1_url = reverse_lazy('delete_label', kwargs={'pk': 1})
        self.delete_task_url = reverse_lazy('delete_task', kwargs={'pk': 1})
        with open(os.path.join('fixtures', 'test_label.json')) as file:
            self.test_label = json.load(file)
        return super().setUp()

    def test_open_labels(self):
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.labels_url)
        self.assertEqual(response.status_code, 200)

    def test_get_create_label(self):
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 200)

    def test_post_create_label(self):
        self.client.force_login(self.user)
        response = self.client.post(self.create_label_url, self.test_label)
        self.assertRedirects(response, self.labels_url, 302)
        self.label = Labels.objects.get(pk=3)
        self.assertEqual(self.label.name, self.test_label.get('name'))

    def test_form_with_data(self):
        label_from = CreateLabelForm(self.test_label)
        self.assertTrue(label_from.is_valid)
        self.assertEqual(len(label_from.errors), 0)

    def test_form_with_empty_data(self):
        label_from = CreateLabelForm({})
        self.assertTrue(label_from.is_valid)
        self.assertEqual(len(label_from.errors), 1)

    def test_get_update_page(self):
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.update_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_update_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.update_pk1_url, self.test_label)
        self.assertEqual(response.status_code, 302)
        self.label = Labels.objects.get(pk=1)
        self.assertEqual(self.label.name, self.test_label.get('name'))

    def test_get_delete_page(self):
        response = self.client.get(self.create_label_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.delete_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete_page(self):
        labels_count = Labels.objects.count()
        self.client.force_login(self.user)
        self.client.post(self.delete_task_url)
        self.client.post(self.delete_pk1_url)
        self.assertEqual(Labels.objects.count(), labels_count - 1)
        with self.assertRaises(Labels.DoesNotExist):
            Labels.objects.get(pk=1)

    def test_cant_delete_with_task(self):
        labels_count = Labels.objects.count()
        self.client.force_login(self.user)
        response = self.client.post(self.delete_pk1_url)
        self.assertEqual(Labels.objects.count(), labels_count)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('It is not possible to delete the label because it is being used', messages)
