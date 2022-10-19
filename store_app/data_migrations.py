def populate_staff_personal_info(apps, schema_editor):
    CustomUser = apps.get_model("accounts_app", "CustomUser")
    Staff = apps.get_model("store_app", "Staff")

    for staff in Staff.objects.all():
        for custom_staff in CustomUser.objects.filter(is_staff=True):
            if staff.email == custom_staff.email:
                staff.personal_info = custom_staff


def populate_customer_personal_info(apps, schema_editor):
    CustomUser = apps.get_model("accounts_app", "CustomUser")
    Customer = apps.get_model("store_app", "Customer")

    for customer in Customer.objects.all():
        for custom_customer in CustomUser.objects.filter(is_staff=False):
            if customer.email == custom_customer.email:
                customer.personal_info = custom_customer