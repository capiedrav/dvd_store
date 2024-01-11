from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Inventory, Rental, Payment, Customer
from movies_app.models import Film
from .forms import UpdateCustomerStoreForm, UpdatePersonalInfoForm, UpdateCustomerAddressForm


# Create your views here.
@login_required(login_url="account_login")
def film_rental_view(request, pk):

    # check film inventory
    film_requested = get_object_or_404(Film, film_uuid=pk)
    customer = get_object_or_404(Customer, personal_info=request.user)  # get the customer trying to rent the film
    # a film is available for rental if it is available in the same store of the customer
    film_inventory = [film for film in Inventory.objects.filter(film=film_requested) if film.available
                      and film.store == customer.store]
    film_available = len(film_inventory) > 0

    if request.method == "POST": # in case of a POST request, i.e. form's button was pressed

        if not film_available: # raise error in case the film is not available for rental (this should never happen)
            raise Http404

        film_for_rental = film_inventory[0] # grab first film available
        film_for_rental.available = False  # mark it as no longer available
        film_for_rental.save(update_fields=["available", ])

        # calculate return date based on rental_date and the rental duration of the film
        rental_date = timezone.datetime.today()
        return_date = rental_date + timezone.timedelta(days=film_requested.rental_duration)

        # get customer and staff info
        # customer = get_object_or_404(Customer, personal_info=request.user)
        staff = film_for_rental.store.manager_staff

        # create new rental record
        new_film_rental = Rental(customer=customer, inventory=film_for_rental, staff=staff, rental_date=rental_date,
                                 return_date=return_date)
        new_film_rental.save()

        # create new payment record
        new_payment = Payment(customer=customer, staff=staff, rental=new_film_rental,
                              amount=film_requested.rental_rate, payment_date=rental_date)
        new_payment.save()

        return redirect(new_payment) # redirect to payment details page

    else: # in case of GET request, display the film rental page
        return render(request, "store_app/film_rental.html", {"film": film_requested, "film_available": film_available})


class FilmPaymentView(LoginRequiredMixin, DetailView):

    model = Payment
    template_name = "store_app/payment_details.html"
    login_url = "account_login" # this the name of the url provided by all-auth app


class CustomerProfileView(LoginRequiredMixin, DetailView):

    model = get_user_model()
    template_name = "store_app/customer_profile.html"
    login_url = "account_login" # this the name of the url provided by all-auth app

    def get_object(self, queryset=None):
        """
        Look up for User instance based in the user_uuid instead of the pk.
        """

        return get_object_or_404(get_user_model(), user_uuid=self.kwargs.get("user_uuid"))

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # all film rentals ordered by most recent rental date
        context["rentals"] = Rental.objects.select_related("inventory").filter(customer=self.request.user.customer).order_by("-rental_date")

        return context


@login_required(login_url="account_login")
def update_customer_profile(request):
    """
    With this view customers can update their profiles.
    """

    if request.method == "POST": # when the form is submitted
        # create bound forms of the respective customer information
        personal_info_form = UpdatePersonalInfoForm(request.POST, instance=request.user)
        customer_store_form = UpdateCustomerStoreForm(request.POST, instance=request.user.customer)
        customer_address_form = UpdateCustomerAddressForm(request.POST, instance=request.user.customer.address)

        # if the information submitted is valid
        if personal_info_form.is_valid() and customer_store_form.is_valid() and customer_address_form.is_valid():
            personal_info_form.save()
            customer_store_form.save()
            customer_address_form.save()

            return redirect(request.user.customer) # redirect to customer profile page

    else: # in case of a GET request (or invalid data submitted)
        # create forms of the respective customer information
        personal_info_form = UpdatePersonalInfoForm(instance=request.user)
        customer_store_form = UpdateCustomerStoreForm(instance=request.user.customer)
        customer_address_form = UpdateCustomerAddressForm(instance=request.user.customer.address)

    # the forms are context variables to be used when rendering the template
    context = {
        "personal_info_form": personal_info_form,
        "customer_store_form": customer_store_form,
        "customer_address_form": customer_address_form
    }

    return render(request, "store_app/update_customer_profile.html", context)




