from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blogapp/<int:blog_id>/', views.detail, name = 'detail'),
    path('blogapp/write/', views.write, name = 'write'),
    path('blogapp/create/', views.create, name = 'create'),
    path('blogapp/newblog/', views.blogpost, name="newblog"),
]