from django.shortcuts import render,redirect
from .forms import LeadAddForm
from authentication.models import *
# from datetime import datetime
from datetime import timezone
import datetime

# Create your views here.


def leaddelete(request,id):
    if request.user.is_authenticated:

        pi=LeadsDuplicate.objects.get(pk=id)
        pi.delete()
        return redirect('dashboard')
    
def leaddetail(request,id):
    if request.user.is_authenticated:
        context={}
        print('user id ',id)
        lead=LeadsDuplicate.objects.get(pk=id)
        calls=Dailycall.objects.filter(call_to_lead_id=id).order_by('calldatetime')

        context['lead']=lead
        context['calls']=calls

        return render(request,'lead/lead_view.html',context)
    else:
        return redirect('userlogin')


def leadedit(request,id):
    if request.user.is_authenticated:
        context={}
        pi=LeadsDuplicate.objects.get(pk=id)
        if request.method == 'POST':
            form=LeadAddForm(request.POST,instance=pi)
            form.save()
            return redirect('dashboard')
        print('pi ',pi.assign_user_id)
        context['lead']=pi
        source=list(Source.objects.all().values('id','name'))
        context['source']=source

        users=list(Users.objects.all().values('id','first_name'))
        context['users']=users
        # print('users',users)

        property_type=list(PropertyType.objects.all().values('id','name'))
        context['property_type']=property_type
        # print('property_type ',property_type)

        response_time=list(ResponseTime.objects.all().values('id','name'))
        context['response_time']=response_time
        # print('response time ',response_time)

        zone_type=list(Zone.objects.all().values('id','title'))
        context['zone_type']=zone_type
        # print('zone_type ',zone_type)

        project_type=list(Project.objects.all().values('id','name'))
        context['project_type']=project_type
        # print('project_type ',project_type)

        budget_type=list(Budget.objects.all().values('id','name'))
        context['budget_type']=budget_type
        # print('budget_type ',budget_type)

        # inventory_type=list(Inventory.objects.all().values('id','name'))
        # context['inventory_type']=inventory_type
        # print('inventory_type ',inventory_type)

        product_type=list(ProductName.objects.all().values('id','name'))
        context['product_type']=product_type
        # print('product_type ',product_type)

        age_group=list(AgeGroup.objects.all().values('id','group'))
        context['age_group']=age_group
        # print('age_group ',age_group)

        working_member=list(WorkingMember.objects.all().values('id','member'))
        context['working_member']=working_member
        # print('working_member ',working_member)

        already_bought_property=list(AlreadyBoughtProperty.objects.all().values('id','name'))
        context['already_bought_property']=already_bought_property
        # print('already_bought_property ',already_bought_property)

        nature_of_lead=list(NatureOfLead.objects.all().values('id','name'))
        context['nature_of_lead']=nature_of_lead
        # print('nature_of_lead ',nature_of_lead)

        number_of_visit=list(NumberOfVisits.objects.all().values('id','visit'))
        context['number_of_visit']=number_of_visit
        # print('number_of_visit ',number_of_visit)

        family_status=list(FamilyStatus.objects.all().values('id','name'))
        context['family_status']=family_status
        # print('family_status ',family_status)

        residential_status=list(ResidentialStatus.objects.all().values('id','name',))
        context['residential_status']=residential_status
        # print('residental_status ',residental_status)

        residential_country=list(Country.objects.all().values('id','name'))
        context['residential_country']=residential_country
        # print('residental_country ',residental_country)

        employment_status=list(EmploymentStatus.objects.all().values('id','status'))
        context['employment_status']=employment_status
        # print('employment_status ',employment_status)


        profession=list(Profession.objects.all().values('id','name'))
        context['profession']=profession
        # print('profession ',profession)


        nature_of_business=list(NatureOfBusiness.objects.all().values('id','name'))
        context['nature_of_business']=nature_of_business
        # print('nature_of_business ',nature_of_business)


        lead_status=list(LeadStatus.objects.all().values('id','name'))
        context['lead_status']=lead_status
        # print('lead_status ',lead_status)

        tracker=list(Tracker.objects.all().values('id','name'))
        context['tracker']=tracker
        # print('tracker ',tracker) 

        builder=list(Builder.objects.all().values('id','name'))
        context['builder']=builder
        # print('builder ',builder) 


        lead_age=list(LeadAge.objects.all().values('id','month'))
        context['lead_age']=lead_age
        print('lead_age ',lead_age) 
        # pi.delete()
        return render(request,'lead/lead_edit.html',context)
    else:
        return redirect('userlogin')



def leadadd(request):
    context={}

    if request.method=="POST":
        form=LeadAddForm(request.POST)
        print('request post', request.POST)
        form.save()

    source=list(Source.objects.all().values('id','name'))
    context['source']=source

    users=list(Users.objects.all().values('id','first_name'))
    context['users']=users
    # print('users',users)

    property_type=list(PropertyType.objects.all().values('id','name'))
    context['property_type']=property_type
    # print('property_type ',property_type)

    response_time=list(ResponseTime.objects.all().values('id','name'))
    context['response_time']=response_time
    # print('response time ',response_time)

    zone_type=list(Zone.objects.all().values('id','title'))
    context['zone_type']=zone_type
    # print('zone_type ',zone_type)

    project_type=list(Project.objects.all().values('id','name'))
    context['project_type']=project_type
    # print('project_type ',project_type)

    budget_type=list(Budget.objects.all().values('id','name'))
    context['budget_type']=budget_type
    # print('budget_type ',budget_type)

    # inventory_type=list(Inventory.objects.all().values('id','name'))
    # context['inventory_type']=inventory_type
    # print('inventory_type ',inventory_type)

    product_type=list(ProductName.objects.all().values('id','name'))
    context['product_type']=product_type
    # print('product_type ',product_type)

    age_group=list(AgeGroup.objects.all().values('id','group'))
    context['age_group']=age_group
    # print('age_group ',age_group)

    working_member=list(WorkingMember.objects.all().values('id','member'))
    context['working_member']=working_member
    # print('working_member ',working_member)

    already_bought_property=list(AlreadyBoughtProperty.objects.all().values('id','name'))
    context['already_bought_property']=already_bought_property
    # print('already_bought_property ',already_bought_property)

    nature_of_lead=list(NatureOfLead.objects.all().values('id','name'))
    context['nature_of_lead']=nature_of_lead
    # print('nature_of_lead ',nature_of_lead)

    number_of_visit=list(NumberOfVisits.objects.all().values('id','visit'))
    context['number_of_visit']=number_of_visit
    # print('number_of_visit ',number_of_visit)

    family_status=list(FamilyStatus.objects.all().values('id','name'))
    context['family_status']=family_status
    # print('family_status ',family_status)

    residential_status=list(ResidentialStatus.objects.all().values('id','name',))
    context['residential_status']=residential_status
    # print('residental_status ',residental_status)

    residential_country=list(Country.objects.all().values('id','name'))
    context['residential_country']=residential_country
    # print('residental_country ',residental_country)

    employment_status=list(EmploymentStatus.objects.all().values('id','status'))
    context['employment_status']=employment_status
    # print('employment_status ',employment_status)


    profession=list(Profession.objects.all().values('id','name'))
    context['profession']=profession
    # print('profession ',profession)


    nature_of_business=list(NatureOfBusiness.objects.all().values('id','name'))
    context['nature_of_business']=nature_of_business
    # print('nature_of_business ',nature_of_business)


    lead_status=list(LeadStatus.objects.all().values('id','name'))
    context['lead_status']=lead_status
    # print('lead_status ',lead_status)

    tracker=list(Tracker.objects.all().values('id','name'))
    context['tracker']=tracker
    # print('tracker ',tracker) 

    builder=list(Builder.objects.all().values('id','name'))
    context['builder']=builder
    # print('builder ',builder) 


    lead_age=list(LeadAge.objects.all().values('id','month'))
    context['lead_age']=lead_age
    print('lead_age ',lead_age) 

    form=LeadAddForm()
    context['leadform']=form
    return render(request,'lead/lead_add.html',context)



def lead_schedule_call(request,id):
    if request.user.is_authenticated:
        context={}
        pi=LeadsDuplicate.objects.get(pk=id)
        if request.method == 'POST':
            form=LeadAddForm(request.POST,instance=pi)
            form.save()
            return redirect('dashboard')
        print('pi ',pi.assign_user_id)
        context['lead']=pi
        source=list(Source.objects.all().values('id','name'))
        context['source']=source

        users=list(Users.objects.all().values('id','first_name'))
        context['users']=users
        # print('users',users)

        property_type=list(PropertyType.objects.all().values('id','name'))
        context['property_type']=property_type
        # print('property_type ',property_type)

        response_time=list(ResponseTime.objects.all().values('id','name'))
        context['response_time']=response_time
        # print('response time ',response_time)

        zone_type=list(Zone.objects.all().values('id','title'))
        context['zone_type']=zone_type
        # print('zone_type ',zone_type)

        project_type=list(Project.objects.all().values('id','name'))
        context['project_type']=project_type
        # print('project_type ',project_type)

        budget_type=list(Budget.objects.all().values('id','name'))
        context['budget_type']=budget_type
        # print('budget_type ',budget_type)

        # inventory_type=list(Inventory.objects.all().values('id','name'))
        # context['inventory_type']=inventory_type
        # print('inventory_type ',inventory_type)

        product_type=list(ProductName.objects.all().values('id','name'))
        context['product_type']=product_type
        # print('product_type ',product_type)

        age_group=list(AgeGroup.objects.all().values('id','group'))
        context['age_group']=age_group
        # print('age_group ',age_group)

        working_member=list(WorkingMember.objects.all().values('id','member'))
        context['working_member']=working_member
        # print('working_member ',working_member)

        already_bought_property=list(AlreadyBoughtProperty.objects.all().values('id','name'))
        context['already_bought_property']=already_bought_property
        # print('already_bought_property ',already_bought_property)

        nature_of_lead=list(NatureOfLead.objects.all().values('id','name'))
        context['nature_of_lead']=nature_of_lead
        # print('nature_of_lead ',nature_of_lead)

        number_of_visit=list(NumberOfVisits.objects.all().values('id','visit'))
        context['number_of_visit']=number_of_visit
        # print('number_of_visit ',number_of_visit)

        family_status=list(FamilyStatus.objects.all().values('id','name'))
        context['family_status']=family_status
        # print('family_status ',family_status)

        residential_status=list(ResidentialStatus.objects.all().values('id','name',))
        context['residential_status']=residential_status
        # print('residental_status ',residental_status)

        residential_country=list(Country.objects.all().values('id','name'))
        context['residential_country']=residential_country
        # print('residental_country ',residental_country)

        employment_status=list(EmploymentStatus.objects.all().values('id','status'))
        context['employment_status']=employment_status
        # print('employment_status ',employment_status)


        profession=list(Profession.objects.all().values('id','name'))
        context['profession']=profession
        # print('profession ',profession)


        nature_of_business=list(NatureOfBusiness.objects.all().values('id','name'))
        context['nature_of_business']=nature_of_business
        # print('nature_of_business ',nature_of_business)


        lead_status=list(LeadStatus.objects.all().values('id','name'))
        context['lead_status']=lead_status
        # print('lead_status ',lead_status)

        tracker=list(Tracker.objects.all().values('id','name'))
        context['tracker']=tracker
        # print('tracker ',tracker) 

        builder=list(Builder.objects.all().values('id','name'))
        context['builder']=builder
        # print('builder ',builder) 


        lead_age=list(LeadAge.objects.all().values('id','month'))
        context['lead_age']=lead_age
        print('lead_age ',lead_age) 
        # pi.delete()
        return render(request,'lead/schedule_call.html',context)
    else:
        return redirect('userlogin')


def schedulehome(request):
    if request.user.is_authenticated:
        context={}
        users=Users.objects.all().values('id','first_name','last_name')
        context['users']=users
        # print('users', users)
        leads=Leads.objects.all()[:200]
        print('leads',leads)
        context['leads']=leads
        schedules=Schedule.objects.all()[:100]
        context['schedules']=schedules
        return render(request,'lead/schedulehome.html',context)
    else:
        return redirect('userlogin')
    

def scheduleAdd(request):
    if request.user.is_authenticated:
        context={}
        leads=Leads.objects.all()[:200]
        # print('leads',leads)
        context['leads']=leads



        if request.method=="POST":
            lead_id=request.POST.get('lead_id')
            print('lead id',lead_id)
            nexttype=request.POST.get('nexttype')
            print('next type',nexttype)
            nextdatetime=request.POST.get('nextdatetime')
            print('next dattime',nextdatetime)
            schedule_by_user=request.user.id
            print('schedule_by_user',schedule_by_user)
            status=0
            # finaldate=datetime.fromisoformat(nextdatetime).astimezone(timezone.utc)
            print('final date',nextdatetime)

            schedule=Schedule(lead_id=lead_id,nexttype=nexttype,nextdatetime=nextdatetime,schedule_by_user=schedule_by_user,status=status)
            
            if(schedule != None):
                print('schedule ',schedule)
                schedule.save()
                return redirect('schedulehome')

            







        return render(request,'lead/scheduleAdd.html',context)
    else:
        return redirect('userlogin')


def leadAssign(request):
    context={}
    leads=Leads.objects.all()[:20]
    context['leads']=leads
    users=Users.objects.all()
    context['users']=users

    return render(request,'lead/lead_assign.html',context)








