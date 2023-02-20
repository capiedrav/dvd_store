from django.urls import path
from .views import film_rental_view, FilmPaymentView, CustomerProfileView, update_customer_profile


urlpatterns = [
    path("film_rental/<uuid:pk>/", film_rental_view, name="film_rental"),
    path("payment_details/<int:pk>/", FilmPaymentView.as_view(), name="payment_details"),
    path("customer_profile/<uuid:user_uuid>/", CustomerProfileView.as_view(), name="customer_profile"),
    path("update_customer_profile/", update_customer_profile, name="update_customer_profile")
]
