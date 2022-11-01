# Generated by Django 3.2.13 on 2022-10-18 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

"""
NOTE: some of the modifications proposed in this migration 
weren't applied fully by Django. So, manual modifications on the database
were necessary. To know what must change use the command sqlmigrate of manage.py
"""

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store_app', '0007_change_foreign_keys_to_integer_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='personal_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='accounts_app.customuser'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='personal_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, primary_key=True, serialize=False, to='accounts_app.customuser'),
        ),

    ]