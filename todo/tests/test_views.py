from django.test import TestCase
from django.urls import reverse

class TodoCreateViewTests(TestCase):
    def test_todo__create_view_has_instance(self):
        response = self.client.get(reverse('todo:create'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/create_todo.html')

class TodoListViewTests(TestCase):
    def test_todo_list_view_has_instance(self):
        response = self.client.get(reverse('todo:list'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

    