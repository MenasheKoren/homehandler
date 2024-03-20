from django.test import TestCase
from .models import Todo

class TodoModelTests(TestCase):
    def test_create_todo_basic_attributes(self):
        todo = Todo.objects.create(
            title='Todo Item 1',
            description='This is the first todo item.',
            completed=False
        )
        self.assertEqual(todo.title, 'Todo Item 1')
        self.assertEqual(todo.description, 'This is the first todo item.')
        self.assertFalse(todo.completed, 'Todo completed should be false by default.')