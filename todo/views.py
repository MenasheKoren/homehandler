from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Todo
from .forms import TodoForm


class CreateTodoView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('home')