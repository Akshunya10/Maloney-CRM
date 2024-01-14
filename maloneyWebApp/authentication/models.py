
# Create your models here.
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class AddLeaseProperty(models.Model):
    product_name = models.CharField(max_length=1000)
    premises_address = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)
    monthly_rent = models.CharField(max_length=500)
    lessee_name = models.CharField(max_length=1000)
    lessor_name = models.CharField(max_length=1000)
    lessee_add = models.CharField(max_length=1000)
    lessor_add = models.CharField(max_length=1000)
    lessee_contact = models.CharField(max_length=11)
    lessor_contact = models.CharField(max_length=11)
    brokerage_day_lessee = models.CharField(max_length=500)
    brokerage_day_lessor = models.CharField(max_length=500)
    brokerage_lessee = models.CharField(max_length=500)
    amount_lessee = models.CharField(max_length=1000)
    pending_lessee = models.IntegerField()
    brokerage_lessor = models.CharField(max_length=500)
    amount_lessor = models.CharField(max_length=1000)
    pending_lessor = models.IntegerField()
    mop_lessee = models.IntegerField()
    mop_lessor = models.IntegerField()
    cash = models.CharField(max_length=1000)
    cash_lessor = models.CharField(max_length=1000)
    brokerage_due = models.CharField(max_length=1000)
    total_amt = models.CharField(max_length=1000)
    pending_amt = models.CharField(max_length=1000)
    bank_name_lessee = models.CharField(max_length=1000)
    date_lessee = models.DateField()
    cheque_lessee = models.CharField(max_length=1000)
    bank_name_lessor = models.CharField(max_length=1000)
    date_lessor = models.DateField()
    cheque_lessor = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'add_lease_property'

class AgeGroup(models.Model):
    group = models.CharField(max_length=300)

    class Meta:
        managed = True
        db_table = 'age_group'


class AlreadyBoughtProperty(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'already_bought_property'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    customer_id = models.IntegerField()
    bank_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    created_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bank'


class BankSchedule(models.Model):
    customer_id = models.IntegerField()
    bank_id = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_by_user = models.IntegerField()
    creation_date = models.DateTimeField()
    modified_by = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank_schedule'


class BookingStatusColor(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'booking_status_color'


class BrokerPayment(models.Model):
    broker_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.IntegerField()
    mode_payment_id = models.IntegerField()
    payment_date = models.DateField()
    bank_name = models.CharField(max_length=500)
    cheque_trans_date = models.IntegerField()
    cheque_number_trans = models.CharField(max_length=200)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'broker_payment'


class Brokerage(models.Model):
    builder_id = models.IntegerField()
    project_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    bsp = models.FloatField()
    additional = models.FloatField()
    total_brokerage = models.FloatField()
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brokerage'


class BrokeragePayment(models.Model):
    brokerage_id = models.IntegerField()
    amount = models.IntegerField()
    mode_payment_id = models.IntegerField()
    bank_name = models.CharField(max_length=200)
    payment_date = models.DateField()
    cheque_trans_date = models.IntegerField()
    cheque_number_trans = models.CharField(max_length=200)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'brokerage_payment'


class BrokeragePaymentPlan(models.Model):
    brokerage_id = models.IntegerField()
    date = models.DateTimeField()
    re_schedule = models.DateTimeField()
    label = models.CharField(max_length=500)
    value = models.CharField(max_length=11)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'brokerage_payment_plan'


class Budget(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'budget'


class Builder(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'builder'


class CallDetails(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'call_details'


class City(models.Model):
    name = models.CharField(max_length=300)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'city'


class CommissionPayment(models.Model):
    broker_id = models.IntegerField()
    property_id = models.IntegerField()
    amount = models.IntegerField()
    mode_payment_id = models.IntegerField()
    bank_name = models.CharField(max_length=300)
    cheque_trans_date = models.DateTimeField()
    cheque_number_trans = models.CharField(max_length=100)
    payment_date = models.DateTimeField()
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commission_payment'


class Country(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'country'


class CustomerAdditionalDetails(models.Model):
    customer_id = models.IntegerField()
    broker_id = models.IntegerField()
    commission_amount = models.IntegerField()
    discount = models.IntegerField()
    builder_discount = models.IntegerField()
    on_form = models.CharField(max_length=200)
    interest_leived = models.IntegerField()
    by_credit_note = models.CharField(max_length=200)
    credit_commission = models.IntegerField()
    net_cost_to_customer = models.IntegerField()
    net_cost_to_builder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_additional_details'


class CustomerAdditionalDetailsBkp(models.Model):
    customer_id = models.IntegerField()
    broker_id = models.IntegerField()
    commission_amount = models.IntegerField()
    discount = models.IntegerField()
    on_form = models.CharField(max_length=200)
    by_credit_note = models.CharField(max_length=200)
    credit_commission = models.IntegerField()
    net_cost_to_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_additional_details-bkp'


class CustomerBooking(models.Model):
    customer_id = models.IntegerField()
    amount = models.FloatField()
    mode_payment_id = models.IntegerField()
    bank_name = models.CharField(max_length=300)
    cheque_trans_date = models.DateTimeField()
    payment_date = models.DateField()
    cheque_number_trans = models.CharField(max_length=100)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_booking'


class CustomerManagement(models.Model):
    lead_id = models.IntegerField()
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=100)
    father_husband_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    c_address = models.CharField(max_length=100)
    city = models.IntegerField()
    pincode = models.IntegerField()
    pan_no = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    dob = models.DateTimeField()
    anniversary_date = models.DateTimeField()
    co_applicant = models.CharField(max_length=250)
    co_applicant_date = models.DateTimeField()
    booking_date = models.DateTimeField()
    plan_id = models.IntegerField()
    plan_type_id = models.IntegerField()
    plan_mode = models.IntegerField()
    loan_interested = models.CharField(max_length=10)
    loan_amount = models.IntegerField()
    loan_status = models.CharField(max_length=10)
    booking_amount_approved = models.IntegerField()
    loan_approved = models.IntegerField()
    other_approved = models.IntegerField()
    booking_status = models.CharField(max_length=50)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_management'


class CustomerPaymentPlan(models.Model):
    customer_id = models.IntegerField()
    date = models.DateTimeField()
    re_schedule = models.DateTimeField()
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=10)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_payment_plan'


class CustomerProductDetails(models.Model):
    customer_id = models.IntegerField()
    builder_id = models.IntegerField()
    project_id = models.IntegerField()
    product_id = models.IntegerField()
    flat_no = models.CharField(max_length=250)
    parking_charges = models.IntegerField()
    plc = models.IntegerField()
    bsp = models.IntegerField()
    edc_idc = models.IntegerField()
    ifms = models.IntegerField()
    club_membership = models.IntegerField()
    power_back_up = models.IntegerField()
    any_other_charges = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_product_details'


class Dailycall(models.Model):
    call_type = models.CharField(max_length=3, blank=True, null=True)
    calldatetime = models.DateTimeField(db_column='calldateTime')  # Field name made lowercase.
    regardingcalldetail = models.TextField(db_column='regardingCallDetail')  # Field name made lowercase.
    call_to_lead_id = models.IntegerField()
    call_by_user = models.IntegerField()
    schedule_id = models.IntegerField(blank=True, null=True)
    project_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dailycall'


class Dashboard(models.Model):
    user_id = models.IntegerField()
    array2 = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'dashboard'


class Delete(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'delete'


class Department(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'department'
    def __str__(self): 
        return self.name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmploymentStatus(models.Model):
    status = models.CharField(max_length=300)
    dependent_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'employment_status'


class ExpenseManagement(models.Model):
    employer_id = models.IntegerField()
    expensetype = models.IntegerField(db_column='expenseType')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectId')  # Field name made lowercase.
    expense_main_id = models.IntegerField()
    expense_date = models.DateTimeField()
    expense_name = models.CharField(max_length=200)
    expense_detail = models.TextField()
    amount = models.FloatField()
    mode_payment_id = models.IntegerField()
    bank_name = models.CharField(max_length=300)
    cheque_trans_date = models.DateTimeField()
    cheque_number_trans = models.CharField(max_length=100)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'expense_management'


class Expensehead(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'expensehead'


class Expensesubhead(models.Model):
    expense_main_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'expensesubhead'


class FamilyStatus(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'family_status'


class GalleryProperty(models.Model):
    property_id = models.IntegerField()
    imagename = models.CharField(db_column='imageName', max_length=350)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gallery_property'


class LeadAge(models.Model):
    month = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'lead_age'


class LeadPhase(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lead_phase'


class LeadStatus(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lead_status'
    
    def __str__(self):
        return self.name
    


class Leads(models.Model):
    prospect_name = models.CharField(max_length=300)
    source = models.IntegerField()
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=300)
    address = models.TextField()
    short_desc = models.CharField(max_length=300, blank=True, null=True)
    assign_user_id = models.IntegerField()
    assigned_by_user_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    assign_date_time = models.DateTimeField(blank=True, null=True)
    accepted_status = models.CharField(max_length=1)
    property_type = models.IntegerField()
    response_time = models.IntegerField()
    zone_type = models.IntegerField(blank=True, null=True)
    project_type = models.IntegerField(blank=True, null=True)
    project_type_multiple = models.CharField(max_length=500)
    budget_type = models.IntegerField(blank=True, null=True)
    inventory_type = models.IntegerField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    created_by_user = models.IntegerField()
    leaddelete = models.CharField(db_column='leadDelete', max_length=1)  # Field name made lowercase.
    modified_date = models.DateTimeField()
    creation_date = models.DateTimeField(blank=True, null=True)
    lessor = models.CharField(max_length=200, blank=True, null=True)
    lessoramount = models.IntegerField(db_column='lessorAmount', blank=True, null=True)  # Field name made lowercase.
    lessordays = models.CharField(db_column='lessorDays', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lessee = models.CharField(max_length=300, blank=True, null=True)
    lesseeamonut = models.IntegerField(db_column='lesseeAmonut', blank=True, null=True)  # Field name made lowercase.
    lesseedays = models.CharField(db_column='lesseeDays', max_length=100, blank=True, null=True)  # Field name made lowercase.
    paydate = models.DateField(db_column='payDate', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.IntegerField(db_column='totalAmount', blank=True, null=True)  # Field name made lowercase.
    pendingamount = models.IntegerField(db_column='pendingAmount', blank=True, null=True)  # Field name made lowercase.
    age_group = models.IntegerField(blank=True, null=True)
    working_member = models.IntegerField()
    already_bought_property = models.IntegerField()
    nature_of_lead = models.IntegerField()
    number_of_visits = models.IntegerField()
    family_status = models.IntegerField()
    residential_status = models.IntegerField()
    residential_country = models.CharField(max_length=300)
    employment_status = models.IntegerField()
    profession = models.IntegerField()
    profession_other = models.CharField(max_length=300)
    nature_of_business = models.IntegerField()
    nob_other = models.CharField(max_length=300)
    lead_status = models.IntegerField()
    tracker = models.IntegerField()
    builder = models.IntegerField()
    lead_age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leads'


class ManageBuilders(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=25)
    address = models.TextField()
    email = models.CharField(unique=True, max_length=255)
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manage_builders'


class ManageProjects(models.Model):
    name = models.CharField(unique=True, max_length=255)
    location = models.CharField(max_length=255)
    project_type_main_id = models.IntegerField()
    builder_id = models.IntegerField()
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manage_projects'


class ManageProperties(models.Model):
    builder_id = models.IntegerField()
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    property_size = models.CharField(max_length=255)
    property_rate = models.CharField(max_length=255)
    property_type_sub_id = models.IntegerField()
    propertytotal = models.FloatField(db_column='propertyTotal')  # Field name made lowercase.
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manage_properties'


class ManagePropertySubType(models.Model):
    main_property_type_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'manage_property_sub_type'


class ManagePropertyType(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'manage_property_type'


class ManageSubBrokers(models.Model):
    company_name = models.CharField(max_length=250)
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    code = models.CharField(unique=True, max_length=200)
    city_id = models.IntegerField()
    created_by_user = models.IntegerField()
    created_date = models.DateTimeField()
    modified_by_user = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'manage_sub_brokers'


class Managelease(models.Model):
    premises_address = models.TextField()
    lessee = models.CharField(max_length=250)
    lesor = models.CharField(max_length=250)
    rent_per_month = models.IntegerField()
    lease_start_date = models.DateTimeField()
    security = models.IntegerField()
    maintenace_charges = models.IntegerField()
    increase_yearly = models.IntegerField()
    service_tax = models.IntegerField()
    property_tax = models.IntegerField()
    agrement_time = models.CharField(max_length=500)
    agreement_sign = models.CharField(max_length=500)
    agreed_reg_charges = models.IntegerField()
    advance_token = models.IntegerField()
    owner_side_pending_work = models.CharField(max_length=500)
    documents_required = models.TextField()
    other_comments = models.TextField()
    witness_1 = models.CharField(max_length=500)
    witness_2 = models.CharField(max_length=500)
    created_by_user = models.IntegerField()
    creation_date = models.DateTimeField()
    modified_by = models.IntegerField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'managelease'


class ModeOfPayment(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'mode_of_payment'


class NatureOfBusiness(models.Model):
    name = models.CharField(max_length=300)
    other_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nature_of_business'


class NatureOfLead(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'nature_of_lead'


class NumberOfVisits(models.Model):
    visit = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'number_of_visits'


class PaymentPlan(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        managed = False
        db_table = 'payment_plan'


class PaymentPlanType(models.Model):
    name = models.CharField(unique=True, max_length=300)

    class Meta:
        managed = False
        db_table = 'payment_plan_type'


class PaymentStatus(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'payment_status'


class Permission(models.Model):
    user_id = models.IntegerField()
    user_permissions = models.TextField()

    class Meta:
        managed = False
        db_table = 'permission'
    def __str__(self) -> str:
        return "UserID- "+ str(self.user_id)


class ProductName(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'product_name'


class Profession(models.Model):
    name = models.CharField(max_length=300)
    other_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profession'


class Project(models.Model):
    name = models.CharField(max_length=200)
    zone_id = models.IntegerField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project'


class ProjectStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'project_status'


class PropertyLease(models.Model):
    product = models.IntegerField()
    size = models.CharField(max_length=350, blank=True, null=True)
    phone_no = models.CharField(max_length=350, blank=True, null=True)
    dimension = models.CharField(max_length=350, blank=True, null=True)
    furnished_type = models.CharField(max_length=1, blank=True, null=True)
    negotiable_price = models.CharField(max_length=1, blank=True, null=True)
    contact_person = models.CharField(max_length=350, blank=True, null=True)
    station = models.CharField(max_length=250)
    sector = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    pic_gallery = models.CharField(max_length=1, blank=True, null=True)
    brokerage = models.CharField(db_column='Brokerage', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sq_ft_price = models.CharField(max_length=350, blank=True, null=True)
    range = models.IntegerField()
    floor_no = models.CharField(max_length=250)
    status = models.CharField(max_length=1)
    sign_age = models.CharField(max_length=1)
    month_rent = models.CharField(max_length=200)
    inventory_available = models.CharField(max_length=1)
    last_auth_date = models.DateField()
    comment = models.CharField(max_length=1000)
    created_by_user = models.IntegerField()
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'property_lease'


class PropertyType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'property_type'


class RangeOptions(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'range_options'


class ResidentialStatus(models.Model):
    name = models.CharField(max_length=300)
    country_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'residential_status'


class ResponseTime(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'response_time'


class Schedule(models.Model):
    lead_id = models.IntegerField()
    schedule_by_user = models.IntegerField()
    nextdatetime = models.DateTimeField(db_column='nextDateTime', blank=True, null=True)  # Field name made lowercase.
    nexttype = models.CharField(db_column='nextType', max_length=1)  # Field name made lowercase.
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'schedule'


class Slabtable(models.Model):
    title = models.CharField(max_length=200)
    val = models.FloatField()

    class Meta:
        managed = False
        db_table = 'slabtable'


class Source(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'source'


class State(models.Model):
    name = models.CharField(max_length=300)
    zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'state'


class Tracker(models.Model):
    name = models.CharField(max_length=300)
    dependent_field = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tracker'



class Users(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    department_id = models.IntegerField()
    users_type = models.IntegerField()
    join_date = models.DateTimeField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'users'
    def __str__(self): 
        return self.first_name

def post_save_django_user_create(instance,sender,*args,**kwargs):
    isUserPresent=User.objects.filter(email=instance.email)
    if(isUserPresent.count()>0):
        djUser=isUserPresent.first()
        djUser.username=instance.email
        djUser.email=instance.email
        djUser.first_name=instance.first_name
        djUser.set_password(instance.password)
        djUser.save()
    else:  
        djUser=User(username=instance.email,email=instance.email,first_name=instance.first_name)
        djUser.set_password(instance.password)
        djUser.save()



    
post_save.connect(post_save_django_user_create,sender=Users)


class Usersession(models.Model):
    session_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'usersession'


class Usertype(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'usertype'
    def __str__(self): 
        return self.title


class WorkingMember(models.Model):
    member = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'working_member'


class Zone(models.Model):
    title = models.CharField(max_length=300)
    country_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone'
