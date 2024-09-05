from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .models import Apartment  # Ensure this is the correct model name
from .forms import CustomLoginForm, ApartmentForm  # Ensure form names are correct
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import View
from .models import Apartment
from .forms import ApartmentForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('account/auth/login')  # Redirect to the login page after logout

def update_apartment(request, id):
    apartment = get_object_or_404(Apartment, pk=id)
    
    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment updated successfully.')
            return redirect('account:apartment')  # Redirect to a suitable page
        else:
            messages.error(request, 'Failed to update the apartment.')
    else:
        form = ApartmentForm(instance=apartment)
    
    context = {
        'apartment': apartment,
        'edit_form': form
    }
    
    return render(request, 'account/admin/apartment.html', context)


   
def delete_apartment(request, id):
    # Fetch the Apartment object or return a 404 if not found
    apartment = get_object_or_404(Apartment, pk=id)
    
    if request.method == 'POST':
        apartment.delete()  # Correctly delete the apartment object
        messages.success(request, 'Apartment deleted successfully.')
        return redirect('account:apartment')  # Redirect to the home or apartment list page after deletion
    
    template_name = 'account/delete_view.html'
    context = {
        'apartment': apartment,  # Pass the correct apartment object to the template
    }
    
    # Render the confirmation template
    return render(request, template_name, context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:dashboard')  # Adjust this to your actual URL name
        else:
            messages.error(request, 'Invalid username or password.')
    form = CustomLoginForm()
    return render(request, 'account/admin/login.html', {'form': form})

# Dashboard View
def dashboardPage(request):
    return render(request, 'account/admin/dashboard.html', {})

# Apartment Page View
class ApartmentPage(View):
    def get(self, request, *args, **kwargs):
        get_apartment_posted = Apartment.objects.all()
        apartment_posted_count = Apartment.objects.count()
        form = ApartmentForm()
        edit_form = ApartmentForm()

        context = {
            'form': form,
            'edit_form': edit_form,
            'apartment_posted': apartment_posted_count,
            'get_apartment_posted': get_apartment_posted
        }
        return render(request, 'account/admin/apartment.html', context)
    
    def post(self, request, *args, **kwargs):
        apartment_id = request.POST.get('apartment_id')
        
        if apartment_id:
            return self.update_apartment(request, apartment_id)
        else:
            return self.create_apartment(request)
    
    def create_apartment(self, request):
        form = ApartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment posted successfully.')
        else:
            messages.error(request, 'Failed to save the apartment.')
        return redirect('account:apartment')
    

# Logout User
def logoutUser(request):
    logout(request)
    return redirect('account:login')  # Adjust this to the actual login URL name
