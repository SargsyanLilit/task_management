from django.urls import path, include
from task import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('task-view/<int:task_id>/', views.task_detail, name='task-view'),
    path('task-delete/<int:task_id>/', views.task_delete, name='task-delete'),
    path('create/', views.task_create, name='task-create'),
    path('task-update/<int:task_id>/', views.task_update, name='task-update'),
]
