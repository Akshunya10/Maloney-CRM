from django.shortcuts import render
from .models import *
# from authentication.forms import UserForm

# Create your views here.
def userlist(request):
    context={}
    departments=Department.objects.all()
    department=[]
    for item in departments:
        department.append(item.name)

    userdata=Users.objects.all()
    context['userdata']=userdata
    context['department']=department
    print('department ',department)
    return render(request,'authentication/userlist.html',context)

# def useradd(request):
#     context={}
#     form=UserForm()
#     context['form']=form
#     return render(request,'authentication/userform.html',context)