# Generated by Django 3.2.13 on 2022-10-18 20:53

from django.db import migrations


def populate_customer_foreign_key(apps, schema_editor):

    Rental = apps.get_model("store_app", "Rental")
    Payment = apps.get_model("store_app", "Payment")
    Customer = apps.get_model("store_app", "Customer")

    # populate foreign keys to customer model
    for rental in Rental.objects.all():
        customer = Customer.objects.get(customer_id=rental.customer_old)
        rental.customer = customer
        rental.save()

    # populate foreign keys to customer model
    for payment in Payment.objects.all():
        customer = Customer.objects.get(customer_id=payment.customer_old)
        payment.customer = customer
        payment.save()


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0011_populate_staff_foreign_key'),
    ]

    operations = [
        migrations.RunPython(populate_customer_foreign_key, reverse_code=migrations.RunPython.noop),
    ]
