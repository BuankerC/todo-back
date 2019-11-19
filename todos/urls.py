from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/api/vl/todos
    path('todos/', views.todo_create),
    # localhost:8000/api/v1/todos/10/
    path('todos/<int:id>/', views.todo_detail),
    path('users/<int:id>/', views.user_detail),
]
