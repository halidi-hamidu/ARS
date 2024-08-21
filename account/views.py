<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Appartment
from .forms import CustomLoginForm, AppartmentForm
from django.contrib import messages

# Login View
=======
from django.shortcuts import render, redirect
from .forms import CustomLoginForm, ApartmentForm
from django.contrib.auth import authenticate, login, logout
from .models import Apartment
from django.contrib import messages
from django.views import View
# Create your views here.
>>>>>>> 8f6516da4c24eb94bb3c7064e58eea2ffd2f51f1
def loginPage(request):
    if request.method == 'POST':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user = authenticate(username=get_username, password=get_password)

        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
    form = CustomLoginForm()
    template_name = 'account/admin/login.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

# Dashboard View
def dashboardPage(request):
    template_name = 'account/admin/dashboard.html'
    context = {}
    return render(request, template_name, context)

<<<<<<< HEAD
# Appartment Page View
def appartmentPage(request):
    appartment_posted_count = Appartment.objects.count()
    form = AppartmentForm()

    if request.method == 'POST':
        form = AppartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'congratulation data saved')        
            return redirect('account:appartment')
        else:
            messages.error(request,'sorry data not saved')
            return redirect('account:appartment')
    form = AppartmentForm()
    get_item_posted = Appartment.objects.all()
    template_name = 'account/admin/appartment.html'
    context = {
        'form': form,
        'appartment_posted': appartment_posted_count,
        'get_item_posted': get_item_posted


    }
    return render(request, template_name, context)
    



#def logoutUser(request):
    logout(request)
    return redirect('account:login')  # Adjust this to the actual login URL name
=======

class ApartmentPage(View):

    def get(self, request, *args, **kwargs):
        get_apartment_posted = Apartment.objects.all()
        Apartment_posted = Apartment.objects.all().count()
        form = ApartmentForm()
        template_name ='account/admin/apartment.html'
        context = {
            'form':form,
            'Apartment_posted':Apartment_posted,
            'get_apartment_posted':get_apartment_posted
        }
        return render(request, template_name, context)#
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ApartmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Success Post saved ')
                return redirect('account:Apartment')
            else:
                messages.error(request, 'POst not saved ')
                return redirect('account:apartment')
>>>>>>> 8f6516da4c24eb94bb3c7064e58eea2ffd2f51f1
