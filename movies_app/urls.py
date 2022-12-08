from django.urls import path
from .views import FilmListView, ActorListView, FilmDetailView, ActorDetailView

urlpatterns = [
    path("films/", FilmListView.as_view(), name="film_list"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("actors/", ActorListView.as_view(), name="actor_list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor_detail"),

]
