from django.test import TestCase
from django.urls import reverse

class TodoCreateViewTests(TestCase):
    def test_todo__create_view_has_instance(self):
        response = self.client.get(reverse('todo:create'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/create_todo.html')
        
    def test_create_todo_item(self):
        post_data = {
            'completed': False,
            'title': 'New Todo',
            'description': 'This is a new todo item.'
        }

        response = self.client.post(reverse('todo:create'), post_data, follow=True)

        self.assertRedirects(response, reverse('todo:list'), status_code=302, target_status_code=200)

class TodoListViewTests(TestCase):
    def test_todo_list_view_has_instance(self):
        response = self.client.get(reverse('todo:list'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

    