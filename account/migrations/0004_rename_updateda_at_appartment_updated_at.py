# Generated by Django 5.1 on 2024-08-20 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_appartment_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appartment',
            old_name='updateda_at',
            new_name='updated_at',
        ),
    ]
