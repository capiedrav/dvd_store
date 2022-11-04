from  django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Create your views here.
class SignupPageView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"

