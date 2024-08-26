# website/models.py
from django.db import models
from django.contrib.auth.models import User

class BillingAddress(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_name} - {self.address}, {self.city}"

class Payment(models.Model):
    CARD_EXP_MONTH_CHOICES = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    exp_year_choices = [(str(year), str(year)) for year in range(2023, 2033)]

    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=19)
    exp_month = models.CharField(max_length=2, choices=CARD_EXP_MONTH_CHOICES)
    exp_year = models.CharField(max_length=4, choices=exp_year_choices)
    cvv = models.CharField(max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.card_name} - {self.card_number}"

class PaymentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.OneToOneField(BillingAddress, on_delete=models.CASCADE)
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment by {self.billing_address.full_name} on {self.date}"
