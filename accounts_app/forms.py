from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm, LoginForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
from django import forms
from .utils import get_stores
from store_app.models import Customer, Address, Store


class CustomUserCreationForm(UserCreationForm):
    """
    form for the creation of a user.
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3(action="user_creation"))

    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """
    form for updating user information.
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3(action="user_change"))

    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomLoginForm(LoginForm):
    """
    Form for user log in.
    """

    captcha = ReCaptchaField(widget=ReCaptchaV3(action="login"))


class CustomSignupForm(SignupForm):
    """
    Form for user sign up.
    """

    store = forms.ChoiceField(choices=get_stores())
    address = forms.CharField(max_length=50)
    district = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)
    captcha = ReCaptchaField(widget=ReCaptchaV3(action="signup"))

    def save(self, request):

        user = super().save(request) # calling superclass method returns the user that just signup

        store = Store.objects.get(store_id=self.cleaned_data["store"])
        customer_address, new_address = Address.objects.get_or_create(address=self.cleaned_data["address"],
                                                                      city=store.address.city)
        if new_address:
            customer_address.district = self.cleaned_data["district"]
            customer_address.phone = self.cleaned_data["phone"]
            customer_address.save()

        # update customer info (the customer instance is already created by using django signals)
        customer = Customer.objects.get(personal_info=user)
        customer.store = store
        customer.address = customer_address

        # update_fields internally issues an update sql statement (avoids race conditions)
        customer.save(update_fields=["store", "address"])

        return user
