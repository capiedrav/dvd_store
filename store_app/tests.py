from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Customer, Staff, Address, Store, City, Country, Inventory, Rental, Payment
from .views import film_rental_view, FilmPaymentView, CustomerProfileView, update_customer_profile
from movies_app.models import Film, Language


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
        address = Address.objects.create(address="123 Elm Street", district="Columbia", city=city, phone="605528858")

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

        # update customer info (the customer instance was created after the user was created using django signals)
        customer = Customer.objects.get(personal_info=customer_info)
        customer.store = store
        customer.address = address
        customer.save(update_fields=["store", "address"])

    def test_customer(self):
        """
        Test correct functioning of Customer model.
        """

        customer = Customer.objects.first()

        self.assertEquals(Customer.objects.count(), 1)
        self.assertEquals(customer.personal_info.username, self.customer_username)
        self.assertEquals(customer.personal_info.email, self.customer_email)
        self.assertEquals(customer.address, Address.objects.first())
        self.assertEquals(customer.store, Store.objects.first())
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

    def test_no_logged_in_customer_cant_access_customer_profile(self):
        """
        Test that no logged-in customer can't access his customer profile page.
        """

        customer_uuid = Customer.objects.first().personal_info.user_uuid

        # make a GET request to the customer profile page
        response = self.client.get(reverse("customer_profile", kwargs={"user_uuid": customer_uuid}))

        # check that the customer is redirected to the login page
        self.assertRedirects(response, expected_url=reverse("account_login") +
                             f"?next=/store/customer_profile/{customer_uuid}/")

        # check that the correct view was used
        self.assertEquals(response.resolver_match.func.__name__, CustomerProfileView.as_view().__name__)

    def test_logged_in_customer_can_access_customer_profile(self):
        """
        Test that a logged-in customer can access his customer profile page.
        """

        customer_uuid = Customer.objects.first().personal_info.user_uuid

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a GET request to the customer profile page
        response = self.client.get(reverse("customer_profile", kwargs={"user_uuid": customer_uuid}))

        # check that the page was successfully accessed
        self.assertEquals(response.status_code, 200)
        # check that the correct template was used
        self.assertTemplateUsed(response, "store_app/customer_profile.html")
        # check that the correct view was used
        self.assertEquals(response.resolver_match.func.__name__, CustomerProfileView.as_view().__name__)

    def test_no_logged_in_customer_cant_update_customer_profile(self):
        """
        Test that no logged-in customer can't update his customer profile.
        """

        # make a GET request to the update customer profile page
        response = self.client.get(reverse("update_customer_profile"))

        # check tha the customer is redirected to the login page
        self.assertRedirects(response, expected_url=reverse("account_login") + "?next=/store/update_customer_profile/")

        # check that the correct view was used
        self.assertEquals(response.resolver_match.func, update_customer_profile)

    def test_logged_in_customer_can_access_update_profile_page(self):

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a GET request to the customer profile page
        response = self.client.get(reverse("update_customer_profile"))

        # check that the page was successfully accessed
        self.assertEquals(response.status_code, 200)
        # check that the correct template was used
        self.assertTemplateUsed(response, "store_app/update_customer_profile.html")
        # check that the correct view was used
        self.assertEquals(response.resolver_match.func, update_customer_profile)

    def test_logged_in_customer_can_update_customer_profile(self):

        customer_uuid = Customer.objects.first().personal_info.user_uuid

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a POST request to the customer profile page
        response = self.client.post(reverse("update_customer_profile"), follow=True)

        # check that the customer is redirected to his profile page
        self.assertRedirects(response, expected_url=reverse("customer_profile", kwargs={"user_uuid": customer_uuid}))


class TestFilmRental(TestCase):

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
        address = Address.objects.create(address="123 Elm Street", district="Columbia", city=city, phone="605528858")

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

        # update customer info (the customer instance was created after the user was created, using django signals)
        customer = Customer.objects.get(personal_info=customer_info)
        customer.store = store
        customer.address = address
        customer.save(update_fields=["store", "address"])

        # setup film data
        language = Language(name="English")
        language.save()

        desc_gone_with_the_wind = "The manipulative daughter of a Georgia plantation owner conducts a turbulent" \
                                  "romance with a roguish profiteer during the American Civil War and Reconstruction" \
                                  "periods."

        Film.objects.create(
            title="Gone with the Wind",
            description=desc_gone_with_the_wind,
            release_year="1939",
            language=language,
            original_language=language,
            rental_duration=3,
            rental_rate=4.99,
            length=221,
            replacement_cost=19.99,
            rating="G"
        )

        desc_the_matrix = "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he" \
                          "discovers the shocking truth--the life he knows is the elaborate deception of an evil" \
                          "cyber-intelligence."

        Film.objects.create(
            title="The Matrix",
            description=desc_the_matrix,
            release_year="1999",
            language=language,
            original_language=language,
            rental_duration=3,
            rental_rate=4.99,
            length=136,
            replacement_cost=19.99,
            rating="R"
        )

        # add films to the inventory
        Inventory.objects.create(
            film=Film.objects.get(title="Gone with the Wind"),
            store=store,
            available=True
        )

        Inventory.objects.create(
            film=Film.objects.get(title="The Matrix"),
            store=store,
            available=False # film not available for rental
        )

    def test_films_inventory(self):

        films_in_inventory = Inventory.objects.all()

        self.assertEquals(len(films_in_inventory), 2)

        # test first film in inventory
        self.assertEquals(films_in_inventory[0].film.title, "Gone with the Wind")
        self.assertTrue(films_in_inventory[0].available)

        # test second film in inventory
        self.assertEquals(films_in_inventory[1].film.title, "The Matrix")
        self.assertFalse(films_in_inventory[1].available) # this film must not be available for rental

    def test_no_logged_in_customer_cant_access_film_rental_page(self):
        """
        Test that no logged-in customer can't access the film rental page. Instead, he is redirected to login page.
        """

        # make a GET request to the film rental page without the customer being logged in
        response = self.client.get(reverse("film_rental", kwargs={"pk": Film.objects.first().film_uuid}))

        # check that customer is redirected to the login page
        self.assertRedirects(response, expected_url=reverse("account_login") +
                             f"?next=/store/film_rental/{Film.objects.first().film_uuid}/")

        self.assertEquals(response.resolver_match.func, film_rental_view) # check for the correct view

    def test_no_logged_in_customer_cant_rent_a_film(self):
        """
        Test that no logged-in customer can't rent a film. Instead, he is redirected to login page.
        """

        # make a POST request to the film rental page without the costumer being logged in
        response = self.client.post(reverse("film_rental", kwargs={"pk": Film.objects.first().film_uuid}))

        # check that the customer is redirected to the login page
        self.assertRedirects(response, expected_url=reverse("account_login") +
                             f"?next=/store/film_rental/{Film.objects.first().film_uuid}/")

        self.assertEquals(response.resolver_match.func, film_rental_view)  # check for the correct view

    def test_logged_in_customer_can_access_film_rental_page(self):
        """
        Test that a logged-in customer can access the film rental page.
        """

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a GET request to the film rental page without the customer being logged in
        response = self.client.get(reverse("film_rental",
                                           kwargs={"pk": Film.objects.get(title="Gone with the Wind").film_uuid}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "store_app/film_rental.html")
        self.assertEquals(response.resolver_match.func, film_rental_view) # check for the correct view

    def test_logged_in_customer_can_rent_a_film(self):
        """
        Test that a logged-in customer can rent a film.
        """

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a POST request to the film rental page
        response = self.client.post(reverse("film_rental",
                                    kwargs={"pk": Film.objects.get(title="Gone with the Wind").film_uuid}), follow=True)

        # check that the customer is redirected to the payment details page
        self.assertRedirects(response, expected_url=reverse("payment_details",
                             kwargs={"pk": Payment.objects.first().payment_id}))

        # check that the rented film is no longer available for rental
        self.assertFalse(Inventory.objects.get(film__title="Gone with the Wind").available)

        # check the template used when redirected
        self.assertTemplateUsed(response, "store_app/payment_details.html")

        # check the view used when redirected
        self.assertEquals(response.resolver_match.func.__name__, FilmPaymentView.as_view().__name__)

    def test_customer_cant_rent_film_when_is_not_available(self):
        """
        When trying to rent an unavailable film, a 404 server error must be raised.
        """

        # login the customer
        self.client.login(email="test_customer@example.com", password="unodostres")

        # make a POST request to the film rental page for a film that is not available for rental
        response = self.client.post(reverse("film_rental",
                                            kwargs={"pk": Film.objects.get(title="The Matrix").film_uuid}))

        self.assertEquals(response.status_code, 404) # there must be a 404 server error
