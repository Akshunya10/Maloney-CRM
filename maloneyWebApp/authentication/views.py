from django.shortcuts import render,redirect,HttpResponse
from .models import *
# from django.contrib.auth.models import User
import datetime
from django.contrib.auth import authenticate,login,get_user_model,logout
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


def userlogin(request):
    if(request.method=="POST"):
        useremail=request.POST.get("useremail")
        password=request.POST.get("password")
        dbuser=Users.objects.filter(email=useremail)
        djangoUser=User.objects.filter(email=useremail)
        print('dj',djangoUser)
        if(djangoUser.count()>0):
            username=djangoUser.first().username
            authUser=authenticate(username=username,password=password)
            print('authuser',authUser)
        # if(dbuser.count()>0):
        #     user=dbuser.first()
            if(authUser):
                login(request,authUser)
                print("login success")
        else:
            print('user not found')

    return render(request,'authentication/userlogin.html')

def useradd(request):
    context={}

    if request.method == 'POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        department=request.POST.get('department')
        usertype=request.POST.get('usertype')
        status=request.POST.get('status')
        joindate= datetime.datetime.now()
        print('firstname',first_name,last_name,email,phone,password,department,usertype,status,joindate)
        if(Users.objects.filter(email=email).count()==0):
            user=Users(first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,department_id=department,users_type=usertype,join_date=joindate,status=status)
            if(user):
                user.save()
                print('user saved', user)
        
                return redirect('/users')

    department=Department.objects.all()
    status=LeadStatus.objects.all()
    usertype=Usertype.objects.all()

    context['department']=department
    context['status']=status
    context['usertype']=usertype


    return render(request,'authentication/useradd.html',context)


def useredit(request,id):
    context={}
    dbuser=Users.objects.filter(id=id).first()
    if request.method == 'POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        department=request.POST.get('department')
        usertype=request.POST.get('usertype')
        status=request.POST.get('status')
        join_date=datetime.datetime.now()
        
        print('firstname',first_name,last_name,email,phone,password,department,usertype,status,dbuser.join_date)
        if(dbuser):

            dbuser.first_name=first_name
            dbuser.last_name=last_name
            dbuser.email=email
            dbuser.phone=phone
            dbuser.password=password
            dbuser.department_id=department
            dbuser.users_type=usertype
            dbuser.status=status
            
            dbuser.save()

        return redirect('/users')

    department=Department.objects.all()
    usertype=Usertype.objects.all()

    context['department']=department
    context['usertype']=usertype
    context['user']=dbuser


    return render(request,'authentication/useredit.html',context)

def userPermission(request,id):
    context={}
    if(request.method=="POST"):
        dbpermissions=Permission.objects.filter(user_id=id)
        if(dbpermissions.count()>0):
            permission_instance=dbpermissions.first()
            permission_data=""
            for item in request.POST.getlist('permissions'):
                permission_data+=item+","
                
            permission_instance.user_permissions=permission_data
            permission_instance.save()

        else:
            permission_data=""
            for item in request.POST.getlist('permissions'):
                permission_data+=item
            permission_instance=Permission(user_id=id,user_permissions=permission_data)
            permission_instance.save()
    
    dbpermissions=Permission.objects.filter(user_id=id).first()
    if(dbpermissions):
        permissions=dbpermissions.user_permissions.split(',')
        context['permissions']=permissions

        return render(request,'authentication/userPermission.html',context)
    return render(request,'authentication/userPermission.html',context)
