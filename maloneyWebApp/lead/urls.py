from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.userlist,name='userlist'),
    path('add/',views.leadadd,name='leadadd'),
    path('edit/<int:id>',views.leadedit,name='leadedit'),
    path('delete/<int:id>',views.leaddelete,name='leaddelete'),
    # path('permission/<int:id>',views.userPermission,name='userpermission'),
    # path('login/',views.userlogin,name="userlogin"),
    # path('dashboard/',views.dashboard,name="dashboard")




]