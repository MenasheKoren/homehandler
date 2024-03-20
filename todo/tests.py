from django.test import TestCase
from .models import Todo

class TodoModelTests(TestCase):
    def setUp(self) -> None:
        self.todo1 = Todo.objects.create(
            title='Todo Item 1',
            description='This is the first todo item.',
            completed=False
        )
        self.todo2 = Todo.objects.create(
            title='Todo Item 2',
            description='This is the second todo item.',
            completed=True
        )
        
    def test_create_todo_basic_attributes(self):
        self.assertEqual(self.todo1.title, 'Todo Item 1')
        self.assertEqual(self.todo1.description, 'This is the first todo item.')
        self.assertFalse(self.todo1.completed)
        self.assertTrue(self.todo2.completed)