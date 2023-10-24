from django.urls import path
from .views import FilmListView, FilmsByCategoryListView,\
    ActorListView, FilmDetailView, ActorDetailView

urlpatterns = [
    path("films/", FilmListView.as_view(), name="film_list"),
    path("action_films/", FilmsByCategoryListView.as_view(), name="action_film_list"),
    path("comedy_films/", FilmsByCategoryListView.as_view(), name="comedy_film_list"),
    path("drama_films/", FilmsByCategoryListView.as_view(), name="drama_film_list"),
    path("films/<uuid:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("actors/", ActorListView.as_view(), name="actor_list"),
    path("actors/<uuid:pk>/", ActorDetailView.as_view(), name="actor_detail"),

]
