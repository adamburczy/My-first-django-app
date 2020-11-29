from django.urls import path
from .views import tasks_all, task_delete, task_detail, task_add, logout_view, user_register, home

urlpatterns = [
    path('', home, name='signuporlogin'),
    path('tasks_all', tasks_all, name='tasks_all'),
    path('delete/<str:title>/', task_delete, name='task_delete'),
    path('detail/<str:title>/', task_detail, name='task_detail'),
    path('add', task_add, name='task_add'),
    path('logout/', logout_view , name='logout'),
    path('register/', user_register, name='register')
]