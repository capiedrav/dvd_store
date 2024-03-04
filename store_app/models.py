from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
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
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
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
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'address'
        verbose_name_plural = "Addresses"
        unique_together = (("address", "city"), )

    def __str__(self):
        return self.address


class Store(models.Model):

    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField('Staff', null=True, related_name="in_charge_of_store",
                                         on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'store'

    def __str__(self):
        return f"Store at {self.address} ({self.address.city} - {self.address.city.country})"


class Staff(models.Model):

    personal_info = models.OneToOneField(CustomUser, primary_key=True, null=False, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    picture = models.BinaryField(blank=True, null=True) # inspectdb initially set this as TextField generating errors
    store = models.ForeignKey(Store, related_name="managed_by", on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'staff'
        verbose_name_plural = "Staff"

    def __str__(self):
        return self.personal_info.username


class Customer(models.Model):

    # NOTE: to avoid this error when trying to create new customers:
    # django.db.utils.OperationalError: (1054, "Unknown column 'create_date' in 'NEW'")
    # delete the create_customer trigger in the database

    store = models.ForeignKey(Store,  null=True, on_delete=models.CASCADE,)
    personal_info = models.OneToOneField(CustomUser, primary_key=True, null=False, on_delete=models.CASCADE,
                                         related_name="customer")
    address = models.ForeignKey(Address,  null=True, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'customer'
        verbose_name_plural = "Customers"

    def get_absolute_url(self):

        return reverse("customer_profile", args=[str(self.personal_info.user_uuid)])

    def __str__(self):
        return self.personal_info.username


class Inventory(models.Model):

    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    available = models.BooleanField(null=False, default=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'inventory'
        verbose_name_plural = "Inventory"

    def __str__(self):
        return f"{self.inventory_id} - {self.film.title}"


class Rental(models.Model):

    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(Staff, null=False, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)

    def __str__(self):
        return "Rental #" + str(self.rental_id)


class Payment(models.Model):

    payment_id = models.SmallAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, null=False, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'payment'

    def get_absolute_url(self):

        return reverse("payment_details", args=[str(self.payment_id)])

    def __str__(self):
        return "Payment # " + str(self.payment_id)
