# Generated by Django 5.1 on 2024-08-19 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_appartment_appartment_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appartment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./media'),
        ),
    ]
