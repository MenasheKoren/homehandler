from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View, DeleteView

from .forms import TodoForm
from .models import Todo


class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('todo:list')


class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list_todo.html'
    context_object_name = 'todos'


class ToggleTodoCompletedView(View):
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs['pk'])
        todo.completed = not todo.completed
        todo.save()
        return HttpResponseRedirect(reverse('todo:list'))


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "todo/update_todo.html"
    fields = ['completed', 'title', 'description']
    success_url = reverse_lazy('todo:list')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')

