# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='Blog home'),
    path("blogpost/<int:id>",views.blogpost,name='Blogpost')
]
