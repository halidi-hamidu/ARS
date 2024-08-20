from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Appartment(models.Model):
    APPARTMENT_TYPE = (
        ('','appartment type'),
        ('Luxury', 'Luxury'),
        ('semi-luxury', 'Semi-luxury'),
        ('normal', 'Normal')
    )
    image = models.ImageField(upload_to='./media',blank=True, null=True)
    appartment_name = models.CharField(max_length=100, blank=True,  default='')
    description =  models.CharField(max_length=500, blank=True,  default='')
    location = models.CharField(max_length=100, blank=True, default='')
    estimated_price = models.CharField(max_length=100, blank=True, default='')
    appartment_type = models.CharField(max_length=100,choices=APPARTMENT_TYPE, default='')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Manage Appartment'

    def __str__(self):
        return str(self.appartment_name)
    