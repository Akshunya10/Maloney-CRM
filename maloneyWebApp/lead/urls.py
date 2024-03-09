from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.userlist,name='userlist'),
    path('add/',views.leadadd,name='leadadd'),
    path('edit/<int:id>',views.leadedit,name='leadedit'),
    path('delete/<int:id>',views.leaddelete,name='leaddelete'),
    path('detail/<int:id>',views.leaddetail,name='leaddetail'),
    path('schedulecall/<int:id>',views.lead_schedule_call,name='schedulecall'),
    path('schedulehome/',views.schedulehome,name='schedulehome'),
    path('scheduleAdd/',views.scheduleAdd,name='scheduleAdd'),
    path('leadassign/',views.leadAssign,name='leadassign'),





    # path('permission/<int:id>',views.userPermission,name='userpermission'),
    # path('login/',views.userlogin,name="userlogin"),
    # path('dashboard/',views.dashboard,name="dashboard")




]