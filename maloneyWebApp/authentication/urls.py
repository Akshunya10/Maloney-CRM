from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userlist,name='userlist'),
    path('add/',views.useradd,name='useradd'),
    path('edit/<int:id>',views.useredit,name='useredit'),


]