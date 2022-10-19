# Generated by Django 3.2.13 on 2022-10-18 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0009_rename_customer_and_staff_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='store_app.customer'),
        ),
        migrations.AddField(
            model_name='payment',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='store_app.staff'),
        ),
        migrations.AddField(
            model_name='rental',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='store_app.customer'),
        ),
        migrations.AddField(
            model_name='rental',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='store_app.staff'),
        ),
        migrations.AddField(
            model_name='store',
            name='manager_staff',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='in_charge_of_store', to='store_app.staff'),
        ),
    ]
