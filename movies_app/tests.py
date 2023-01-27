from django.test import TestCase
from .models import Language, Film, Actor
from .views import FilmListView, FilmDetailView, ActorListView, ActorDetailView
from django.urls import reverse

"""
Run these tests using:

python manage.py test --settings=project_config.tests_settings

to avoid errors with migrations during test database setup.

Check project_config/tests_settings.py for more info.
"""


# Create your tests here.
class FilmTests(TestCase):
    """
    Test for Film model.
    """

    def setUp(self):

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

    def test_films_in_the_database(self):

        all_films = Film.objects.all().order_by("last_update")

        self.assertEquals(len(all_films), 2)
        self.assertEquals(all_films[0].title, "Gone with the Wind")
        self.assertEquals(all_films[1].title, "The Matrix")

    def test_film_list_view(self):

        response = self.client.get(reverse("film_list")) # do a GET request to the film list url

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "movies_app/film_list.html") # check for the correct html template
        # check for the correct view
        self.assertEquals(response.resolver_match.func.__name__, FilmListView.as_view().__name__)

    def test_film_detail_view(self):

        # do a GET request to the film detail url (passing the pk of a film)
        response = self.client.get(reverse("film_detail", kwargs={"pk": Film.objects.first().film_uuid}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "movies_app/film_detail.html") # check for the correct html template
        # check for the correct view
        self.assertEquals(response.resolver_match.func.__name__, FilmDetailView.as_view().__name__)


class ActorTest(TestCase):
    """
    Tests for Actor model.
    """

    def setUp(self):

        Actor.objects.create(first_name="Clark", last_name="Gable")
        Actor.objects.create(first_name="Keanu", last_name="Reeves")

    def test_actors_in_the_database(self):

        all_actors = Actor.objects.all().order_by("last_update")

        self.assertEquals(len(all_actors), 2)
        self.assertEquals(all_actors[0].first_name, "Clark")
        self.assertEquals(all_actors[0].last_name, "Gable")
        self.assertEquals(all_actors[1].first_name, "Keanu")
        self.assertEquals(all_actors[1].last_name, "Reeves")

    def test_actors_list_view(self):

        response = self.client.get(reverse("actor_list")) # do a GET request to the actor list url

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "movies_app/actor_list.html") # check for the correct html template
        # check for the correct view
        self.assertEquals(response.resolver_match.func.__name__, ActorListView.as_view().__name__)

    def test_actor_detail_view(self):

        response = self.client.get(reverse("actor_detail", kwargs={"pk": Actor.objects.first().actor_uuid}))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "movies_app/actor_detail.html")
        self.assertEquals(response.resolver_match.func.__name__, ActorDetailView.as_view().__name__)
