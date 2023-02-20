from django.forms import ModelForm, EmailInput
from django.contrib.auth import get_user_model
from .models import Customer, Address


class UpdatePersonalInfoForm(ModelForm):

    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name"]
        widgets = {
            "email": EmailInput(attrs={"readonly": "readonly"}) # email field is readonly (not editable by the customer)
        }


class UpdateCustomerStoreForm(ModelForm):

    class Meta:
        model = Customer
        fields = ["store", ]


class UpdateCustomerAddressForm(ModelForm):

    class Meta:
        model = Address
        fields = ["address", "phone"]

