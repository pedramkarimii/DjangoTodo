# Add Func
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_say_hello, name="home"),
    path('hello/', views.say_hello, name="hello"),
    path('detail/<int:TODO_ID>/', views.detail, name="detail"),
    path('delete/<int:TODO_ID>/', views.delete, name="delete"),
    path('update/<int:TODO_ID>/', views.update, name="update"),
    path('creat/', views.creat_todo, name="creat"),
]
