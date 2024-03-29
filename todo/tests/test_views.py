from django.test import TestCase
from django.urls import reverse

class CreateTodoViewTests(TestCase):
    def test_todo_create_view_has_instance(self):
        response = self.client.get(reverse('todo:create'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/create_todo.html')