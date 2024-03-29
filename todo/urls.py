from django.urls import path
from .views import CreateTodoView

app_name = 'todo'

urlpatterns = [
    path('create/', CreateTodoView.as_view(), name='create'),
]