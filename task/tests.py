from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from task.models import Task


# Create your tests here.

class TaskTestCase(APITestCase):
    def setUp(self):
        # Instance APIClient
        self.client = APIClient()
        # Create user and token
        self.user = User.objects.create_superuser(username="test", email="test@test.com", password="prueba123.")
        Token.objects.create(user=self.user)

        self.task_data = {"name": "New task!"}
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_task_create(self):
        """
        Create task
        """
        self.response = self.client.post(reverse("post_tasks"), self.task_data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_task_get_all(self):
        """
        Get list of task
        """
        Task.objects.create(name="Test task", status=False, owner=self.user)
        Task.objects.create(name="Test task 2", status=False, owner=self.user)
        self.response = self.client.get(reverse("users_task"), format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(self.response.data), 2)

    def test_task_update(self):
        """
        Update a task
        """
        task = Task.objects.create(name="Test task", status=False, owner=self.user)
        self.response = self.client.put(reverse("tasks", kwargs={"pk": task.pk}), self.task_data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_task_delete(self):
        """
        Delete a task
        """
        task = Task.objects.create(name="Test task", status=False, owner=self.user)
        self.response = self.client.delete(reverse("tasks", kwargs={"pk": task.pk}), self.task_data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_user(self):
        """
        Create a user
        """
        new_user = {"username": "new_user_test", "password": "hi123."}
        self.response = self.client.post(reverse("users"), new_user, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_delete_user(self):
        """
        Delete a user
        """
        user = User.objects.create_user(username="test4", password="hi123.")
        self.response = self.client.delete(reverse("users_detail", kwargs={"pk": user.pk}), format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)