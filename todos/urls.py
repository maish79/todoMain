from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="one"),
    path('add/<str:pk>', views.addTask, name="add"),
    path('delete/<str:pk>', views.deleteTask, name="delete"),
]