from django.contrib import admin
from .models import Country, City, Address, Store, Staff, Customer, Inventory, Rental, Payment


class CustomerAdmin(admin.ModelAdmin):
    """
    Settings for displaying model Customer in admin site.
    """

    list_select_related = True
    # display_username, display_first_name, display_last_name, display_email are the methods defined below
    list_display = ("display_username", "display_first_name", "display_last_name", "display_email", "store")
    list_filter = ("store",)
    search_fields = ["personal_info__username", "personal_info__first_name", "personal_info__last_name",
                     "personal_info__email"]

    @admin.display(description="USERNAME")
    def display_username(self, customer_instance):
        return customer_instance.personal_info.username

    @admin.display(description="FIRST NAME")
    def display_first_name(self, customer_instance):
        return customer_instance.personal_info.first_name

    @admin.display(description="LAST NAME")
    def display_last_name(self, customer_instance):
        return customer_instance.personal_info.last_name

    @admin.display(description="EMAIL")
    def display_email(self, customer_instance):
        return customer_instance.personal_info.email


class InventoryAdmin(admin.ModelAdmin):
    """
    Settings for displaying Inventory model in admin site.
    """

    list_select_related = True # use select_related when querying this model in admin site
    ordering = ("inventory_id", )
    list_display = ("inventory_id", "film", "store", "available")
    list_filter = ("store", "available")
    search_fields = ["film__title"]


class RentalAdmin(admin.ModelAdmin):
    """
    settings for displaying Rental model in admin site.
    """

    list_select_related = True
    list_display = ("rental_id", "display_film_title", "display_inventory", "display_customer_username",
                    "display_staff", "rental_date", "display_store")
    list_filter = ("inventory__store",)
    fields = ("inventory", "customer", "staff", "rental_date", "return_date")
    readonly_fields = ("customer", "staff", "inventory", "rental_date", "return_date")
    search_fields = ["inventory__film__title", "customer__personal_info__username", "staff__personal_info__username"]

    @admin.display(description="FILM")
    def display_film_title(self, rental_instance):
        return rental_instance.inventory.film.title

    @admin.display(description="INVENTORY ID")
    def display_inventory(self, rental_instance):
        return rental_instance.inventory.inventory_id

    @admin.display(description="USERNAME")
    def display_customer_username(self, rental_instance):
        return rental_instance.customer.personal_info.username

    @admin.display(description="STAFF")
    def display_staff(self, rental_instance):
        return rental_instance.staff.personal_info.username

    @admin.display(description="STORE")
    def display_store(self, rental_instance):
        return rental_instance.inventory.store


# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Store)
admin.site.register(Staff)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(Payment)
