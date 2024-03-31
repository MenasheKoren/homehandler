from django.test import TestCase
from django.urls import reverse

class CreateTodoViewTests(TestCase):
    def test_create_todo_view_has_instance(self):
        response = self.client.get(reverse('todo:create'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/create_todo.html')

class ListTodoViewTests(TestCase):
    def test_list_todo_view_has_instance(self):
        response = self.client.get(reverse('todo:list'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

    