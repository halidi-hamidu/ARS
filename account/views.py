from django.shortcuts import render, redirect
from .forms import CustomLoginForm, ApartmentForm
from django.contrib.auth import authenticate, login, logout
from .models import Apartment
from django.contrib import messages
from django.views import View
# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user = authenticate(username=get_username, password = get_password)

        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
    forms = CustomLoginForm()
    template_name ='account/admin/login.html'
    context = {
        'form':forms
    }
    return render(request, template_name, context)



def dashboardPage(request):
    template_name ='account/admin/dashboard.html'
    context = {
        
    }
    return render(request, template_name, context)


class ApartmentPage(View):

    def get(self, request, *args, **kwargs):
        get_apartment_posted = Apartment.objects.all()
        Apartment_posted = Apartment.objects.all().count()
        form = ApartmentForm()
        template_name ='account/admin/Apartment.html'
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
                return redirect('account:Apartment')
