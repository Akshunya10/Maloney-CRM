from django.shortcuts import render,redirect
from .models import *
import datetime
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


def customernewupdate(request,id): 
    if request.user.is_admin:
        if request.method=="POST":
            pi=CustomerNew.objects.get(pk=id)
            form=CustomerNewForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,"successful")
                return redirect('addcustomernew')

        pi=CustomerNew.objects.get(pk=id)
        form=CustomerNewForm(instance=pi)
        return render(request,'authentication/updatecustomernew.html',{'form':form})
    else:
        return redirect('userlogin')