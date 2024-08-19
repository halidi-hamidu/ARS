from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Appartment
class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'


class AppartmentForm(ModelForm):
    class Meta:
        model = Appartment
        fields = '__all__'
        exclude =[
            'uploaded_by'
        ]