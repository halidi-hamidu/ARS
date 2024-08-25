from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm

# Login View
def loginPage(request):
    if request.method == 'POST':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user = authenticate(username=get_username, password=get_password)

        if user is not None:
            login(request, user)
            return redirect('website:dashboard')  # Adjust this to your actual URL name

    form = CustomLoginForm()
    template_name = 'website/login.html'
    context = {'form': form}
    return render(request, template_name, context)

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
            messages.success(request, "Registration successful.")   

            return redirect('website:loginPage') 
        else:
            messages.error(request, "There were errors with your submission.")

            return redirect('website:register')
    else:
        form = SignUpForm()
    
    return render(request, 'website/register.html', {'form': form})

def dashboard(request):
        template_name = 'website/dashboard.html'
        context = {}
        return render(request, template_name, context)

def apartment(request):
        template_name ='website/properties.html'
        context ={}
        return render(request,template_name, context)

def paymentPage(request):
        template_name ='website/payment1.html'
        context ={}
        return render(request,template_name, context)