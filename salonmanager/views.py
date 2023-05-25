from django.urls import reverse
from decimal import Decimal
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Service, Product, Package
from customerapp.models import StaffMember, Appointment,Customer,Branch
from .forms import PackageUpdateForm,ProductForm,ServiceForm,PackageForm,CustomerForm
from .utils import calculate_end_time,timeslot_gen,timeslot_gen_tf
from datetime import datetime, timedelta, timezone
from django.utils import timezone
from datetime import date
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def manager_signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('manager_login')
    return render (request,'manager_signup.html')

def manager_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            
            return redirect('book_appointment')
        else:
            return redirect('manager_login')
    return render (request,'manager_login.html')
   



#@login_required(login_url='manager_login')
def manager_dashboard(request):
    return render(request, 'dashboard.html')

#@login_required(login_url='manager_login')
def list_services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

#@login_required(login_url='manager_login')
def create_service(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_services')
    return render(request, 'create_service.html', {'form': form})

@login_required(login_url='manager_login')
def update_service(request, pk):
    service = Service.objects.get(id=pk)
    form = ServiceForm(instance=service)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('list_services')
    return render(request, 'update_service.html', {'form': form})

@login_required(login_url='manager_login')
def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('list_services')
    return render(request, 'delete_service.html', {'service': service})

#@login_required(login_url='manager_login')
def list_product(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

#@login_required(login_url='manager_login')
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    return render(request, 'create_product.html', {'form': form})

@login_required(login_url='manager_login')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    return render(request, 'update_product.html', {'form': form})

def appointment(request):
    return render(request,'appointment.html')

@login_required(login_url='manager_login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_product')
    return render(request, 'delete_product.html', {'product': product})

#@login_required(login_url='manager_login')


def list_package(request):
    packages = Package.objects.all()
    return render(request, 'package_list.html', {'packages': packages})


def update_package(request, pk):
    package = get_object_or_404(Package, id=pk)
    if request.method == 'POST':
        form = PackageUpdateForm(request.POST, instance=package)
        if form.is_valid():
            form.save()
            return redirect('list_package')  # Redirect to the package list view
    else:
        form = PackageUpdateForm(instance=package)
    return render(request, 'update_package.html', {'form': form, 'package': package})


def create_package(request):
    services=Service.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.created_at = timezone.now()  # Set the value for created_at
            package.updated_at = timezone.now()
            package.save()
            form.save_m2m()  # Save the many-to-many field
            return redirect('list_package')
    else:
        form = PackageForm()
    return render(request, 'create_package.html', {'form': form,'services':services})

def delete_package(request, pk):
    package = get_object_or_404(Package, id=pk)
    if request.method == 'POST':
        package.delete()
        return redirect('list_package')  # Redirect to the package list view
    return render(request, 'delete_package.html', {'package': package})

def list_customer(request):
    customers = Customer.objects.all()
    return render(request, 'list_customer.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customer')  # Redirect to the customer list view
    else:
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form})

def update_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_customer')  # Redirect to the customer list view
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'update_customer.html', {'form': form, 'customer': customer})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('list_customer')  # Redirect to the customer list view
    return render(request, 'delete_customer.html', {'customer': customer})


def book_appointment(request):
    appointment_list_d=[]
    appointment_list=[]
    staff_members=[]
    branches=[]
    today = datetime.now()
    formatted_date = today.strftime("%Y-%m-%d")
    if request.method == 'POST':
        date = request.POST.get('date')
        branch_id = request.POST.get('branch')
        formatted_date = datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')
        appointment_list_d = Appointment.objects.filter(date=formatted_date,branch = branch_id)
        staff_members = StaffMember.objects.filter(branches = branch_id )
        branches = Branch.objects.filter(id = branch_id)
    else:
        
        if Appointment.objects.exists:
            appointment_list_d = Appointment.objects.filter(date=formatted_date)
        branches = Branch.objects.all()
        staff_members = StaffMember.objects.all()
        
    print(appointment_list_d)
    for appointment in appointment_list_d:
        customer_id = appointment.customer_id
        customer  = get_object_or_404(Customer,id = customer_id)
        staff_member_id = appointment.staff_member_id
        staff_member = get_object_or_404(StaffMember,id = staff_member_id)
        branch_id = appointment.branch_id
        branch = get_object_or_404(Branch,id=branch_id)
        
        appointment_dict={
                'customer':customer,
                'staff_member':staff_member,
                'start_time':appointment.start_time.strftime('%I:%M %p'),
                'end_time':appointment.end_time,
                'date':appointment.date,
                'total_price':appointment.total_price,
                'status':appointment.status,
                'branch':branch,
                'id':appointment.pk
            }
        appointment_list.append(appointment_dict)   
    time_slots_12f = timeslot_gen('10:00 AM','10:00 PM')
    time_slots_24f = timeslot_gen_tf('10:00 AM','10:00 PM')
    time_slots=[]
    for i in range(len(time_slots_12f)):
        time_slot_dict = {
            'time_12f':time_slots_12f[i],
            'time_24f':time_slots_24f[i]
        }
        time_slots.append(time_slot_dict)
    booked_list=[]
    completed_list=[]
    confirmed_list=[]
    cancelled_list=[]
    for app in appointment_list:
        if app['status'] == 'booked':
            booked_list.append(app)
        if app['status'] == 'completed':
            completed_list.append(app)
        if app['status'] == 'confirm':
            confirmed_list.append(app)
        if app['status'] == 'cancelled':
            cancelled_list.append(app)
            
            
    
    no_of_booked = len(booked_list)
    no_of_cancelled=len(cancelled_list)
    no_of_completed = len(completed_list)
    no_of_confirmed = len(confirmed_list)
    number_of_app = {
        'booked_app':no_of_booked,
        'cancelled_app':no_of_cancelled,
        'completed_app':no_of_completed,
        'confirmed_app':no_of_confirmed
    }

    
    return render(request, 'dashboard.html',{'staff_members': staff_members,'time_slots':time_slots,'appointment_details_list':appointment_list,'branches':branches,'number_of_app' :number_of_app})
def create_appointment(request):
     global appointment_text
     services = Service.objects.all()
     customer_list = Customer.objects.all()
     if request.method == "POST":
         staff = request.POST.get('staff-name')
         staff_member=get_object_or_404(StaffMember, id=staff)
         print(staff_member)
         start_time = request.POST.get('start-time')
         branch_id = request.POST.get('branch')
         
         print('at create appoitnment'+start_time)
         
         date = request.POST.get('date')
         branch = get_object_or_404(Branch,id = branch_id)
         appointment_text= {
            'staff_member': staff_member,
            'date': date,
            'start_time': start_time,
            'branch':branch
        }
     
     context = {'appointment_details':appointment_text, 'services':services,'customer_list':customer_list} 
     
     return render(request, 'create_appointment.html',context)
def display_bill(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff-name')
        staff_member=get_object_or_404(StaffMember, id=staff_id)
        start_time = request.POST.get('start-time')
        customer_id = request.POST.get('customer_name')
        branch_id = request.POST.get('branch')
        branch = get_object_or_404(Branch,id = branch_id)
        date = request.POST.get('date')
        selected_services = request.POST.getlist('services')
        service_durations = []
        service_names = []
        total_duration = timedelta()
        total_prices=[]
        service_details=[]
        for service_id in selected_services:
            
            service = Service.objects.get(id=service_id)
            service_durations.append(service.duration)
            total_duration =total_duration+service.duration
            total_prices.append(service.price)
            service_names.append(service.name)
            service_details.append(service)
        end_time = calculate_end_time(start_time, total_duration)
    
       
        customer_name  = get_object_or_404(Customer, id=customer_id)
# Convert to 12-hour format with AM/PM
        
    
        total_price = sum([Decimal(str(price.amount)) for price in total_prices])
        print(total_price)
        bill_details = {
            'start_time':start_time,
            'end_time':end_time,
            'customer_name':customer_name,
            'services':service_details,
            'total_price':total_price,
            'date': date,
            'staff_member':staff_member,
            'branch':branch
        }
    
        
    return render(request,'display_bill.html', bill_details)
def booked_appointment(request):
    global branch
    appointment_list=[]
    staff_members=[]
    if request.method == "POST":
        customer_id = request.POST.get('customer_name')
        customer = get_object_or_404(Customer, id=customer_id)
        staff = request.POST.get('staff_member')
        staff_member = get_object_or_404(StaffMember, id=staff)
       
    
        total_price = request.POST.get('price')
        services_ids = request.POST.getlist('services')
        services = Service.objects.filter(id__in=services_ids) 
        branch_id =request.POST.get('branch')
        branch = get_object_or_404(Branch, id = branch_id)
        start = request.POST.get('start_time')
        end = request.POST.get('end_time')
       
       
        date_booked  =  request.POST.get('date')
        formatted_date = datetime.strptime(date_booked, '%d-%m-%Y').strftime('%Y-%m-%d')
        appointment_details = Appointment.objects.create(
            customer=customer,
            staff_member=staff_member,
            start_time=start,
            end_time=end,
            date=formatted_date,
            total_price = total_price,
            status = 'booked',
            branch = branch
            
        )
    
        
        appointment_details.services.set(services)
        
        appointment_list_d=Appointment.objects.filter(date =formatted_date,branch = branch_id )
        for appointment in appointment_list_d:
            print(appointment.start_time)
            appointment_dict={
                'customer':appointment.customer,
                'staff_member':appointment.staff_member,
                'start_time':appointment.start_time.strftime('%I:%M %p'),
                'end_time':appointment.end_time,
                'date':appointment.date,
                'total_price':appointment.total_price,
                'status':appointment.status,
                'branch':appointment.branch,
                'id':appointment.pk
            }
            appointment_list.append(appointment_dict)
        staff_members = StaffMember.objects.filter(branches=branch)
        print(appointment_list)
    time_slot_tf = timeslot_gen_tf('10:00 AM','10:00 PM')
   
    time_slots_t =  timeslot_gen('10:00 AM','10:00 PM')
    time_slots=[]
    booked_list=[]
    completed_list=[]
    confirmed_list=[]
    cancelled_list=[]
    for i in range(len(time_slots_t)):
        time_slots_dict={
            'time_24f':time_slot_tf[i],
            'time_12f':time_slots_t[i]
        }
        time_slots.append(time_slots_dict)
    for app in appointment_list:
        if app['status'] == 'booked':
            booked_list.append(app)
        if app['status'] == 'completed':
            completed_list.append(app)
        if app['status'] == 'confirm':
            confirmed_list.append(app)
        if app['status'] == 'cancelled':
            cancelled_list.append(app)
            
            
            
    branches = Branch.objects.all()
    no_of_booked = len(booked_list)
    no_of_cancelled=len(cancelled_list)
    no_of_completed = len(completed_list)
    no_of_confirmed = len(confirmed_list)
    number_of_app = {
        'booked_app':no_of_booked,
        'cancelled_app':no_of_cancelled,
        'completed_app':no_of_completed,
        'confrimed_app':no_of_confirmed
    }
   
    
    
    return render(request, 'dashboard.html',{'staff_members': staff_members,'branches':branches, 'appointment_details_list':appointment_list,'time_slots':time_slots,'time_slot_tf':time_slot_tf,'number_of_app' :number_of_app} )

def change_appointment(request):
    list_id=[]
    global selected_option
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        selected_option= request.POST.get('option')
        list_id = appointment_id.split() 
        print(list_id[1])
        appointment = Appointment.objects.get(id=list_id[1])
        print(appointment)
        setattr(appointment, 'status', selected_option)
        appointment.save()
        return redirect('book_appointment')

        
    return HttpResponse(status=200)
    