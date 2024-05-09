from django.test import TestCase
from django.urls import reverse

from ..models import Todo


class TodoIntegrationTests(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(title="Buy groceries", description="Milk, Eggs, Bread", completed=False)

    def test_todo_addition_and_display(self):
        response = self.client.post(reverse('todo:create'), {
            'title': 'Walk the dog',
            'description': 'Evening walk in the park',
            'completed': False
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

        self.assertContains(response, 'Walk the dog')
        self.assertContains(response, 'Evening walk in the park')

    def test_mark_todo_completed(self):
        response = self.client.get(reverse('todo:toggle', args=[self.todo.id]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

        self.assertNotContains(response, 'Not Completed')
        self.assertContains(response, 'Completed')

    def test_update_todo(self):
        updated_data = {
            'title': 'Buy groceries and toiletries',
            'description': 'Milk, Eggs, Bread, and Shampoo',
            'completed': True
        }

        response = self.client.post(reverse('todo:update', args=[self.todo.id]), data=updated_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

        self.assertContains(response, 'Buy groceries and toiletries')
        self.assertContains(response, 'Milk, Eggs, Bread, and Shampoo')
        self.assertContains(response, 'Completed')

    def test_delete_todo(self):
        response = self.client.post(reverse('todo:delete', args=[self.todo.id]), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

        self.assertNotContains(response, 'Buy groceries')
