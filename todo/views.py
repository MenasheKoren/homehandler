from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Todo
from .forms import TodoForm


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('todo:list')


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list_todo.html'
    context_object_name = 'todos'
