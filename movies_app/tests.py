from django.test import TestCase
from .models import Language, Film, Actor

"""
Run these tests using:

python manage.py test --settings=project_config.tests_settings

to avoid errors with migrations during test database setup.

Check project_config/tests_settings.py for more info.
"""


# Create your tests here.
class FilmTests(TestCase):

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

        self.assertEquals(Film.objects.count(), 2)
        self.assertEquals(Film.objects.get(pk=1).title, "Gone with the Wind")
        self.assertEquals(Film.objects.get(pk=2).title, "The Matrix")
