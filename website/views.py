from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm

def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('login')  
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'website/login.html', {'form': form})


def homePage(request):
    template_name = 'website/index.html'
    context = {

    }
    return render( request, template_name, context)

def properties(request):
    template_name = 'website/properties.html'
    context={}
    return render( request, template_name, context)

def about(request):
    template_name = 'website/about.html'
    context={}
    return render( request, template_name, context)
def contact(request):
    template_name = 'website/contact.html'
    context={}
    return render( request, template_name, context)

def team(request):
    template_name = 'website/team.html'
    context={}
    return render( request, template_name, context)

def blog(request):    
    template_name = 'website/blog.html'
    context={}
    return render( request, template_name, context)

def testimonials(request):
    template_name = 'website/testimonials.html'
    context={}
    return render( request, template_name, context)

def terms(request):
    template_name = 'website/terms.html'
    context={}
    return render( request, template_name, context)

def property_details(request):
    template_name = 'website/property_details.html'
    context={}
    return render( request, template_name, context)


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, "There were errors with your submission.")
    else:
        form = SignUpForm()
    
    return render(request, 'website/register.html', {'form': form})