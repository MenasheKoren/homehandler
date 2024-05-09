from django.test import TestCase

from ..forms import TodoForm


class TodoFormTests(TestCase):
    def test_todo_form_has_instance(self):
        form = TodoForm()
        self.assertIsInstance(form, TodoForm)

    def test_todo_form_has_fields(self):
        form = TodoForm()
        self.assertTrue(
            len(form.fields) > 0, 'TodoForm should have at least one field.')

    def test_todo_form_field_presence(self):
        form = TodoForm()
        expected_fields = ['completed', 'title', 'description']
        actual_fields = list(form.fields)
        self.assertCountEqual(expected_fields, actual_fields,
                              'Form fields do not match actual fields.')

    def test_todo_form_data_validation(self):
        form_data = {
            'completed': False,
            'title': 'Todo Form Item 1',
            'description': 'This is the first todo form item.',
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid(), 'Form is not valid.')

    def test_todo_form_error_handling(self):
        form_data = {
            'completed': False,
            'title': '',
            'description': 'This is the first todo form item.',
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid(), 'Form should be invalid')
        self.assertIn('title', form.errors)
