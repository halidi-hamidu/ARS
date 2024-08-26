from django.contrib import admin

# Register your models here.
# website/admin.py
from django.contrib import admin
from .models import BillingAddress, Payment

admin.site.register(BillingAddress)
admin.site.register(Payment)
# admin.site.register(PaymentHistory)

