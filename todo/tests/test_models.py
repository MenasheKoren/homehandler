from django.test import TestCase
from ..models import Todo


class TodoModelTests(TestCase):
    def setUp(self) -> None:
        self.todo1 = Todo.objects.create(
            title='Todo Item 1',
            description='This is the first todo item.',
            completed=False
        )

    def test_create_todo_basic_attributes(self):
        self.assertEqual(self.todo1.title, 'Todo Item 1')
        self.assertEqual(self.todo1.description,
                         'This is the first todo item.')
        self.assertFalse(self.todo1.completed,
                         'Todo completed should be false by default.')

    def test_marking_todo_as_completed_sets_completed_at(self):
        self.todo1.completed = True
        self.todo1.save()

        self.todo1.refresh_from_db()

        self.assertTrue(self.todo1.completed,
                        'Todo should be marked as completed.')
        self.assertIsNotNone(
            self.todo1.completed_at, 'completed_at should be set when a task is completed.')

    def test_created_at_is_set_on_todo_creation(self):
        self.assertIsNotNone(
            self.todo1.created_at, 'created_at should be automatically set on creation.')
