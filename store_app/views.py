from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Inventory, Rental, Payment, Customer
from movies_app.models import Film


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

        # rent first film available in the inventory
        film_for_rental = film_inventory[0]
        film_for_rental.available = False  # mark it as no longer available
        film_for_rental.save()

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
