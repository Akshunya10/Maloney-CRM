from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.userlist,name='userlist'),
    path('add/',views.useradd,name='useradd'),
    path('edit/<int:id>',views.useredit,name='useredit'),
    path('permission/<int:id>',views.userPermission,name='userpermission'),
    path('login/',views.userlogin,name="userlogin"),
    path('dashboard/',views.dashboard,name="dashboard")




]