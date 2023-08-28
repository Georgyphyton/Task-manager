from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse_lazy
from users.models import CustomUser
from tasks.models import Tasks
from tasks.forms import CreateTaskForm
from django.contrib.messages import get_messages
import os
import json


class Testtasks(TestCase):
    fixtures = ['statuses.json', 'users.json', 'tasks.json', 'labels.json']

    def setUp(self):
        self.client = Client()
        self.login_url = reverse_lazy('login')
        self.tasks_url = reverse_lazy('tasks')
        self.create_task_url = reverse_lazy('create_task')
        self.task1 = Tasks.objects.get(pk=1)
        self.task2 = Tasks.objects.get(pk=2)
        self.user = CustomUser.objects.get(pk=1)
        self.task_url = reverse_lazy('task', kwargs={'pk': 1})
        self.update_pk1_url = reverse_lazy('update_task', kwargs={'pk': 1})
        self.delete_pk1_url = reverse_lazy('delete_task', kwargs={'pk': 1})
        self.delete_pk2_url = reverse_lazy('delete_task', kwargs={'pk': 2})
        with open(os.path.join('fixtures', 'test_task.json')) as file:
            self.test_task = json.load(file)
        return super().setUp()

    def test_open_task(self):
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, 200)

    def test_open_tasks(self):
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 200)

    def test_filter_tasks(self):
        self.client.force_login(self.user)
        response = self.client.get(self.tasks_url)
        self.assertIn(self.task1, response.context_data['tasks'])
        response = self.client.get(self.tasks_url, data={'status': '2'})
        self.assertNotIn(self.task1, response.context_data['tasks'])

    def test_get_create_page(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 200)

    def test_post_create_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.create_task_url, self.test_task)
        self.assertRedirects(response, self.tasks_url, 302)
        self.task = Tasks.objects.get(pk=3)
        self.assertEqual(self.task.name, self.test_task.get('name'))

    def test_form_with_data(self):
        task_from = CreateTaskForm(self.test_task)
        self.assertTrue(task_from.is_valid)
        self.assertEqual(len(task_from.errors), 0)

    def test_form_with_empty_data(self):
        task_from = CreateTaskForm({})
        self.assertTrue(task_from.is_valid)
        self.assertEqual(len(task_from.errors), 2)

    def test_get_update_page(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.update_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_update_page(self):
        self.client.force_login(self.user)
        response = self.client.post(self.update_pk1_url, self.test_task)
        self.assertEqual(response.status_code, 302)
        self.task = Tasks.objects.get(pk=1)
        self.assertEqual(self.task.name, self.test_task.get('name'))

    def test_get_delete_page(self):
        response = self.client.get(self.create_task_url)
        self.assertEqual(response.status_code, 302)
        self.client.force_login(self.user)
        response = self.client.get(self.delete_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete_page(self):
        task_count = Tasks.objects.count()
        self.client.force_login(self.user)
        self.client.post(self.delete_pk1_url)
        self.assertEqual(Tasks.objects.count(), task_count - 1)
        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(pk=1)

    def test_cant_delete_task_if_not_autor(self):
        task_count = Tasks.objects.count()
        self.client.force_login(self.user)
        response = self.client.post(self.delete_pk2_url)
        self.assertEqual(Tasks.objects.count(), task_count)
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('A task can only be deleted by its author', messages)
