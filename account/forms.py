from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Apartment
class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class ApartmentForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        exclude =[
            'uploaded_by'
        ]