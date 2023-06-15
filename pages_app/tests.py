from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

"""
Run these tests using:

python manage.py test --settings=project_config.tests_settings

to avoid errors with migrations during test database setup.

Check project_config/tests_settings.py for more info.
"""


# Create your tests here.
class HomePageTests(TestCase):

    def setUp(self):

        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):

        self.assertEquals(self.response.status_code, 200)

    def test_homepage_template(self):

        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):

        self.assertContains(self.response, "DVD Store")

    def test_homepage_does_not_contain_incorrect_html(self):

        self.assertNotContains(self.response, "Netflix")

    def test_homepage_url_resolves_homepageview(self):

        view = resolve("/")

        self.assertEquals(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    """
    Tests for about page.
    """

    def setUp(self):

        url = reverse("about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_aboutpage_template(self):

        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):

        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):

        self.assertNotContains(self.response, "Home Page")

    def test_about_page_resolves_aboutpageview(self):

        view = resolve("/about/")

        self.assertEquals(view.func.__name__, AboutPageView.as_view().__name__)

