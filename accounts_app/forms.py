from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django import forms
from .utils import get_stores
from store_app.models import Customer, Address, Store


class CustomUserCreationForm(UserCreationForm):
    """
    form for the creation of a user.
    """

    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """
    form for updating user information.
    """

    class Meta:
        model = get_user_model()
        fields = ("username", "email")


class CustomSignupForm(SignupForm):

    store = forms.ChoiceField(choices=get_stores())
    address = forms.CharField(max_length=50)
    district = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=20)

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
        customer.save()

        return user
