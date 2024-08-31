from django.contrib import admin

# Register your models here.
# website/admin.py
from django.contrib import admin
from .models import BillingAddress, Payment ,House

admin.site.register(BillingAddress)
admin.site.register(Payment)
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'location', 'status', 'email', 'contact_number', 'map_url', 'size', 'image_name')


# admin.site.register(PaymentHistory)

