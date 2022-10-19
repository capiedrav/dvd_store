from django.db import models
from django.contrib.auth import get_user_model
from movies_app.models import Film


CustomUser = get_user_model()


class Country(models.Model):

    country_id = models.SmallAutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'country'
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country


class City(models.Model):

    city_id = models.SmallAutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'city'
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city


class Address(models.Model):

    address_id = models.SmallAutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    location = models.TextField()  # This field type is a guess.
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'address'
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField('Staff', null=True, related_name="in_charge_of_store",
                                         on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'store'

    def __str__(self):
        return "Store #" + str(self.store_id)


class Staff(models.Model):

    personal_info = models.OneToOneField(CustomUser, primary_key=True, null=False, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    picture = models.BinaryField(blank=True, null=True) # inspectdb initially set this as TextField generating errors
    store = models.ForeignKey(Store, related_name="managed_by", on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'staff'
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.personal_info.first_name + " " + self.personal_info.last_name


class Customer(models.Model):

    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    personal_info = models.OneToOneField(CustomUser, primary_key=True, null=False, on_delete=models.RESTRICT)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.personal_info.first_name + " " + self.personal_info.last_name


class Inventory(models.Model):

    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.RESTRICT)
    store = models.ForeignKey(Store, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'inventory'
        verbose_name_plural = "Inventory"

    def __str__(self):
        return "Inventory #" + str(self.inventory_id)


class Rental(models.Model):

    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.RESTRICT)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(Staff, null=False, on_delete=models.RESTRICT)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)

    def __str__(self):
        return "Rental #" + str(self.rental_id)


class Payment(models.Model):

    payment_id = models.SmallAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.RESTRICT)
    staff = models.ForeignKey(Staff, null=False, on_delete=models.RESTRICT)
    rental = models.ForeignKey(Rental, on_delete=models.RESTRICT, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'payment'

    def __str__(self):
        return "Payment # " + str(self.payment_id)
