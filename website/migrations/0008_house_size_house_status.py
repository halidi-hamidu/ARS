# Generated by Django 5.0.7 on 2024-08-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_image_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='status',
            field=models.CharField(choices=[('sale', 'For Sale'), ('rent', 'For Rent')], default='sale', max_length=4),
        ),
    ]
