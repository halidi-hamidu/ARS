from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django import forms
from .models import BillingAddress, Payment
from collections import OrderedDict
from django.utils.translation import gettext_lazy as _

# Custom field definitions
class CreditCardNumberField(forms.CharField):
       """
    A form field for validating credit card expiration dates.
    The expected format is MM/YY.
    """

class CreditCardExpiryField(forms.CharField):
      """
    A form field for validating credit card expiration dates.
    The expected format is MM/YY.
    """

class CreditCardVerificationField(forms.CharField):
    pass  # Replace with actual implementation

class CreditCardNameField(forms.CharField):
    pass  # Replace with actual implementation

class PaymentForm(forms.Form):
    """
    Payment form, suitable for Django templates.

    When displaying the form remember to use *action* and *method*.
    """

    def __init__(
        self,
        data=None,
        action="",
        method="post",
        provider=None,
        payment=None,
        hidden_inputs=True,
        autosubmit=False,
    ):
        if hidden_inputs and data is not None:
            super().__init__(auto_id=False)
            for key, val in data.items():
                widget = forms.widgets.HiddenInput()
                self.fields[key] = forms.CharField(initial=val, widget=widget)
        else:
            super().__init__(data=data)
        self.action = action
        self.autosubmit = autosubmit
        self.method = method
        self.provider = provider
        self.payment = payment

class CreditCardPaymentForm(PaymentForm):
    number = CreditCardNumberField(label=_("Card Number"), max_length=32, required=True)
    expiration = CreditCardExpiryField(label=_("Expiration"))
    cvv2 = CreditCardVerificationField(
        label=_("CVV2 Security Number"),
        required=False,
        help_text=_(
            "Last three digits located on the back of your card."
            " For American Express the four digits found on the front side."
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, hidden_inputs=False, **kwargs)
        if hasattr(self, "VALID_TYPES"):
            self.fields["number"].valid_types = self.VALID_TYPES

class CreditCardPaymentFormWithName(CreditCardPaymentForm):
    name = CreditCardNameField(label=_("Name on Credit Card"), max_length=128)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name_field = self.fields.pop("name")
        fields = OrderedDict({"name": name_field})
        fields.update(self.fields)
        self.fields = fields


# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['card_name', 'card_number', 'exp_month', 'exp_year', 'cvv', 'amount']
#         widgets = {
#             'card_number': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Card Number'}),
#             'cvv': forms.TextInput(attrs={'type': 'password', 'placeholder': 'CVV'}),
#             'exp_month': forms.Select(attrs={'class': 'form-control'}),
#             'exp_year': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
#         }

# class BillingAddressForm(forms.ModelForm):
#     class Meta:
#         model = BillingAddress
#         fields = ['full_name', 'email', 'address', 'city', 'state', 'zip_code']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'city': forms.TextInput(attrs={'class': 'form-control'}),
#             'state': forms.TextInput(attrs={'class': 'form-control'}),
#             'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
#         }



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        
        # Ensure user exists
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Invalid username or password.")

        return cleaned_data


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
    