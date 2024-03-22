from django.test import TestCase
from ..forms import TodoForm

class TestFormTests(TestCase):
    def test_todo_form_has_instance(self):
        form = TodoForm()
        self.assertIsInstance(form, TodoForm)

    def test_todo_form_has_fields(self):
        form = TodoForm()
        self.assertIsNotNone(len(form.fields), 'TodoForm should have at least one field.')

    def test_todo_form_field_presence(self):
        form = TodoForm()
        expected_fields = ['completed', 'title', 'description']
        actual_fields = list(form.fields)
        self.assertCountEqual(expected_fields, actual_fields, 'Form fields do not match actual fields.')

