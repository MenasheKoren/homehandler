from django.urls import path
from .views import TodoCreateView, TodoListView, ToggleTodoCompletedView, TodoUpdateView

app_name = 'todo'

urlpatterns = [
    path('create/', TodoCreateView.as_view(), name='create'),
    path("list/", TodoListView.as_view(), name="list"),
    path("todo/<int:pk>/toggle/", ToggleTodoCompletedView.as_view(), name="toggle"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="update"),
]
