from django.urls import path
from .views import film_rental_view, FilmPaymentView


urlpatterns = [
    path("film_rental/<uuid:pk>/", film_rental_view, name="film_rental"),
    path("payment_details/<int:pk>/", FilmPaymentView.as_view(), name="payment_details"),
]
