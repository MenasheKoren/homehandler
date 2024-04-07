from django.test import TestCase
from django.urls import reverse

from ..models import Todo


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

        response = self.client.post(
            reverse('todo:create'), post_data, follow=True)

        self.assertRedirects(response, reverse('todo:list'),
                             status_code=302, target_status_code=200)


class TodoListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo1 = Todo.objects.create(
            completed=False,
            title='Todo 1',
            description='This is the first todo item.'
        )
        cls.todo2 = Todo.objects.create(
            completed=True,
            title='Todo 2',
            description='This is the second todo item.'
        )
        return super().setUpTestData()

    def test_todo_list_view_has_instance(self):
        response = self.client.get(reverse('todo:list'))
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/list_todo.html')

    def test_empty_todo_list_message(self):
        Todo.objects.all().delete()
        response = self.client.get(reverse('todo:list'))
        self.assertContains(response, 'No todos available.')

    def test_list_view_displays_items(self):
        response = self.client.get(reverse('todo:list'))
        self.assertContains(response, "Not Completed", html=True)
        self.assertContains(response, self.todo1.title)
        self.assertContains(response, self.todo1.description)
        self.assertContains(response, "Completed", html=True)
        self.assertContains(response, self.todo2.title)
        self.assertContains(response, self.todo2.description)


class TodoUpdateViewTests(TestCase):
    def setUp(self) -> None:
        self.todo = Todo.objects.create(
            completed=False,
            title='Sample todo',
            description='This is a sample todo.'
        )

    def test_toggle_completed_todo_status(self):
        self.assertEqual(self.todo.completed, False)
        self.client.get(reverse('todo:toggle', args=[self.todo.id]))
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.completed, True)

    def test_redirect_after_toggle(self):
        response = self.client.get(reverse('todo:toggle', args=[self.todo.id]))
        self.assertRedirects(response, reverse('todo:list'))
