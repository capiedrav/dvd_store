from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Customer, Staff, Address, Store, City, Country

"""
Run these tests using:

python manage.py test --settings=project_config.tests_settings

to avoid errors with migrations during test database setup.

Check project_config/tests_settings.py for more info.
"""


# Create your tests here.
class TestCustomersAndStaff(TestCase):
    """
    Test Customer and Staff models
    """

    def setUp(self):

        CustomUser = get_user_model()
        self.customer_username = "test_customer"
        self.customer_email = "test_customer@example.com"
        self.staff_username = "test_staff"
        self.staff_email = "test_staff@example.com"

        # personal info of the customer
        customer_info = CustomUser.objects.create_user(username=self.customer_username, email=self.customer_email,
                                                       password="unodostres")

        # personal info of the staff
        staff_info = CustomUser.objects.create_user(username=self.staff_username, email=self.staff_email,
                                                    password="unodostres", is_staff=True)

        # boiler-plate models needed for Staff and Customer models
        country = Country.objects.create(country="United States")
        city = City.objects.create(city="Washington", country=country)
        address = Address.objects.create(address="123 Elm Street", district="Columbia", city=city)

        # To correctly save Staff and Store models in the database:

        # 1. save store instance
        store = Store(address=address)
        store.save()

        # 2. save staff instance
        staff = Staff(personal_info=staff_info, address=address, store=store)
        staff.save()

        # 3. update manager_staff and save again
        store.manager_staff = staff
        store.save()

        # save customer
        Customer.objects.create(personal_info=customer_info, store=store, address=address)

    def test_customer(self):
        """
        Test correct functioning of Customer model.
        """

        customer = Customer.objects.first()

        self.assertEquals(Customer.objects.count(), 1)
        self.assertEquals(customer.personal_info.username, self.customer_username)
        self.assertEquals(customer.personal_info.email, self.customer_email)
        self.assertEquals(customer.address.address, Address.objects.first().address)
        self.assertFalse(customer.personal_info.is_staff)

    def test_staff(self):
        """
        Test correct functioning of Staff model.
        :return:
        """

        staff = Staff.objects.first()

        self.assertEquals(Staff.objects.count(), 1)
        self.assertEquals(staff.personal_info.username, self.staff_username)
        self.assertEquals(staff.personal_info.email, self.staff_email)
        self.assertEquals(staff.address.address, Address.objects.first().address)
        self.assertTrue(staff.personal_info.is_staff)
