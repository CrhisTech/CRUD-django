from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_task/', views.create_task),
    path('edit_task/<int:task_id>/', views.edit_task),
    path('delete_task/<int:task_id>/', views.delete_task),
]
