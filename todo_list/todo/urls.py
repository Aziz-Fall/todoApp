from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete_task/<int:pk>", views.delete_task, name="delete_task"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("task_done/<int:pk>", views.task_done, name="task_done"),
]
