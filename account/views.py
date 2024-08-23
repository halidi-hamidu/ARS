from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Apartment  # Note: Ensure model name matches your actual model
from .forms import CustomLoginForm, ApartmentForm  # Note: Ensure form name matches your actual form
from django.contrib import messages
from django.views import View

# Login View
def loginPage(request):
    if request.method == 'POST':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user = authenticate(username=get_username, password=get_password)

        if user is not None:
            login(request, user)
            return redirect('account:dashboard')  # Adjust this to your actual URL name

    form = CustomLoginForm()
    template_name = 'account/admin/login.html'
    context = {'form': form}
    return render(request, template_name, context)

# Dashboard View
def dashboardPage(request):
    template_name = 'account/admin/dashboard.html'
    context = {}
    return render(request, template_name, context)

# Apartment Page View
class ApartmentPage(View):

    def get(self, request, *args, **kwargs):
        get_apartment_posted = Apartment.objects.all()
        apartment_posted_count = Apartment.objects.all().count()
        form = ApartmentForm()
        template_name = 'account/admin/apartment.html'
        context = {
            'form': form,
            'apartment_posted': apartment_posted_count,
            'get_apartment_posted': get_apartment_posted
        }
        return render(request, template_name, context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ApartmentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Success Post saved ')
                return redirect('account:apartment')  # Ensure URL name matches
            else:
                messages.error(request, 'Post not saved ')
                return redirect('account:apartment')

# Logout User
def logoutUser(request):
    logout(request)
    return redirect('account:login')  # Adjust this to the actual login URL name

