from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    APARTMENT_TYPE_CHOICES = (
        ('Luxury', 'Luxury'),
        ('Semi-luxury', 'Semi-luxury'),
        ('Normal', 'Normal')
    )
    
    image = models.ImageField(upload_to='apartments/%Y/%m/%d/', blank=True, null=True)
    apartment_name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=500, blank=True, default='')
    location = models.CharField(max_length=100, blank=True, default='')
    estimated_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    apartment_type = models.CharField(max_length=100, choices=APARTMENT_TYPE_CHOICES, blank=True, default='')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Manage Apartments'

    def __str__(self):
        return str(self.apartment_name)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.apartment.apartment_name} Booking"
