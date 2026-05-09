from django.urls import path
from . import views

app_name = 'kanban'

urlpatterns = [
    path('', views.board, name='board'),
    path('add/<int:column_id>/', views.add_task, name='add_task'),
    path('move/<int:task_id>/<str:direction>/', views.move_task, name='move_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
