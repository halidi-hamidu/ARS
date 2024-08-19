from django.shortcuts import render, redirect
from .forms import CustomLoginForm, AppartmentForm
from django.contrib.auth import authenticate, login, logout
from .models import Appartment
from django.contrib import messages
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


def appartmentPage(request):
    if request.method == 'POST':
        form = AppartmentForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success Post saved ')
            return redirect('account:appartment')
        else:
            messages.error(request, 'POst not saved ')
            return redirect('account:appartment')
    else:
        get_item_posted = Appartment.objects.all()
        appartment_posted = Appartment.objects.all().count()
        form = AppartmentForm()
        template_name ='account/admin/appartment.html'
        context = {
            'form':form,
            'appartment_posted':appartment_posted,
            'get_item_posted':get_item_posted
        }
        return render(request, template_name, context)