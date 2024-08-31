# from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm
from django.shortcuts import redirect, render , get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomLoginForm
# website/views.py
from .forms import BillingAddressForm, PaymentForm
# from .models import PaymentHistory
# from .models import PaymentHistory
from .models import *

# def property_list(request):
#     houses = House.objects.all()
#     return render(request, 'website/property_list.html', {'houses': houses})


def payment_history(request):
    # Query the PaymentHistory model to get the payment history for the user
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'website/payment_history.html', {'payments': payments})


def paymentPage(request):
    if request.method == 'POST':
        billing_form = BillingAddressForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if billing_form.is_valid() and payment_form.is_valid():
            # Save forms to get instances
            billing_address = billing_form.save()
            payment = payment_form.save()

            # Compute the amount here
            amount = compute_amount()  # Replace with actual computation or retrieval
            if billing_address and payment :
                print("---------",billing_address)
            # Create PaymentHistory instance

                # PaymentHistory.objects.create(
                #     user=request.user,
                #     billing_address=billing_address,
                #     payment=payment,
        
                #     amount=amount,
                # )
                messages.success(request, "Payment successfully processed!")
                return redirect('website:dashboard')  # Redirect after successful form submission
            else:
                messages.success(request, "Paymen Erorr!")
                return redirect('website:dashboard')  # Redirect after successful form submission



    else:
        billing_form = BillingAddressForm()
        payment_form = PaymentForm()

    return render(request, 'website/payment1.html', {
        'form': billing_form,
        'payment_form': payment_form,
    })

def compute_amount():
    # Example function to compute amount
    return 100.00  # 


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

def property_details(request, id):
    get_property = get_object_or_404(House, pk=id)
    template_name = 'website/property_details.html'
    context={
        'house':get_property
    }
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
        get_user_history = Payment.objects.filter(user = request.user)
        context = {
            'get_user_history':get_user_history
        }
        return render(request, template_name, context)

def apartment(request):
        get_houses= House.objects.all()

        template_name ='website/properties.html'
        context ={
            'houses':get_houses 
        }
        return render(request,template_name, context)

def payment_history(request, id):
        payment_history = get_object_or_404(PaymentHistory, id=id)
        template_name = 'website/payment_history.html'
        context={}
        return render(request,template_name, context)