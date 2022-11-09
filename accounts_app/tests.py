from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


"""
Run these tests using:

python manage.py test --settings=project_config.tests_settings

to avoid errors with migrations during test database setup.

Check project_config/tests_settings.py for more info.
"""


# Create your tests here.
class CustomUserTests(TestCase):
    """
    This class tests user creation functionality.
    """

    def setUp(self):
        self.user_model = get_user_model()
        self.username = "john"
        self.email = "john@example.com"

        self.admin = "jim"
        self.admin_email = "jim.admin@email.com"

        # create user
        self.user_model.objects.create_user(username=self.username, email=self.email, password="unodostres")

        # create superuser
        self.user_model.objects.create_superuser(username=self.admin, email=self.admin_email, password="unodostres")

    def test_create_user(self):

        # retrieve user from database
        user = self.user_model.objects.first()

        # test for data integrity
        self.assertEquals(self.user_model.objects.count(), 2)
        self.assertEquals(user.username, self.username)
        self.assertEquals(user.email, self.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        # retrieve superuser from database
        superuser = self.user_model.objects.last()

        # test for data integrity
        self.assertEquals(self.user_model.objects.count(), 2)
        self.assertEquals(superuser.username, self.admin)
        self.assertEquals(superuser.email, self.admin_email)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_superuser)


class SignupPageTests(TestCase):
    """
    This class tests user sign up functionality.
    """

    def setUp(self):

        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_sign_up_template(self):

        self.assertEquals(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Sign In")

