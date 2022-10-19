from django.contrib import admin
from .models import Country, City, Address, Store, Staff, Customer, Inventory, Rental, Payment


# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(Inventory)
admin.site.register(Rental)
admin.site.register(Payment)
