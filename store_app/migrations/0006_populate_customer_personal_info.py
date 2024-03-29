# Generated by Django 3.2.13 on 2022-10-18 01:49

from django.db import migrations


def populate_customer_personal_info(apps, schema_editor):
    """
    Link Customer model with CustomUser model.

    Comparing emails is one way to assure that model entries are linked correctly.
    """

    CustomUser = apps.get_model("accounts_app", "CustomUser")
    Customer = apps.get_model("store_app", "Customer")

    # iterate over all customers
    for customer in Customer.objects.all():
        customer_email = customer.email.lower().split("@")[0] # get the first part of the email (before the @)
        # iterate over CustomUser entries that are not staff (i.e., they're customers)
        for custom_customer in CustomUser.objects.filter(is_staff=False):
            custom_customer_email = custom_customer.email.split("@")[0] # get the first part of the email (before the @)
            if customer_email == custom_customer_email: # if both entries represent the same user
                customer.personal_info = custom_customer # link them
                customer.save() # save entry back to the database
                break


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_populate_staff_personal_info'),
        ('accounts_app', '0003_copy_customer_info'),
    ]

    operations = [
        migrations.RunPython(populate_customer_personal_info, reverse_code=migrations.RunPython.noop),
    ]
