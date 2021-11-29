from django.urls import path 

from .import views

app_name = 'core'

urlpatterns = [
    path('todo/', views.display_tasks, name='todo'),
    path('task_list/', views.task_list, name='task_list'),
    path('check/', views.check, name='check'),

    path('lodolist/', views.TodoList.as_view(), name='todolist'),
    path('addtodo/', views.add_todo, name='addtodo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('undo_todo/<int:pk>/', views.undo_todo, name='undo_todo'),
    path('complete_todo/<int:pk>/', views.complete_todo, name='complete_todo'),
    path('edit_todo/<int:pk>/edit/', views.edit_todo, name='edit_todo'),
    path('after_edit/', views.after_edit, name='after_edit'),

    path('task/', views.get_task, name='task'),

]