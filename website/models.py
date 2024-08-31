# website/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name} - {self.address}, {self.city}, {self.state}, {self.zip_code}"



class PaymentHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    billing_address = models.OneToOneField('BillingAddress', on_delete=models.CASCADE)
    payment = models.OneToOneField('Payment', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Payment History'
        verbose_name_plural = 'Payment Histories'

    def __str__(self):
        return f"Payment by {self.user.username} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CC', 'Credit Card'),
        ('PP', 'PayPal'),
        ('BT', 'Bank Transfer'),
    ]
    
    PAYMENT_STATUSES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('F', 'Failed'),
        ('R', 'Refunded'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUSES, default='P')
    transaction_id = models.CharField(max_length=255, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} ({self.get_method_display()})"

    def is_successful(self):
        return self.status == 'C'


class House(models.Model):
    STATUS_CHOICES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]
    name = models.CharField(max_length=100, default='Name')
    location = models.CharField(max_length=100, default='location')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(default="Descriptions")
    image_name = models.ImageField(upload_to='images/',default='path/to/default/image.jpg')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='sale')
    size = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    email = models.EmailField(max_length=254, default='example@example.com')  # Added email field
    contact_number = models.CharField(max_length=15, default='000-000-0000')  # Added contact number field
    map_url = models.CharField(max_length=800, default='http://maps.google.com/')  # Added map URL field

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')  # Renamed from image_name

    def __str__(self):
        return self.name

