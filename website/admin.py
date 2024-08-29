from django.contrib import admin

# Register your models here.
# website/admin.py
from django.contrib import admin
from .models import BillingAddress, Payment ,House

admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(House)

# admin.site.register(PaymentHistory)

