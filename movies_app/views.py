from django.views.generic import ListView, DetailView
from .models import Film, Actor, FilmActor


# Create your views here.
class FilmListView(ListView):

    model = Film
    template_name = "movies_app/film_list.html"


class FilmDetailView(DetailView):

    model = Film
    template_name = "movies_app/film_detail.html"
    context_object_name = "film"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # get all actors in this film
        actors_in_this_film = FilmActor.objects.filter(film=context["film"])
        context["all_actors"] = []

        for actor in actors_in_this_film:
            context["all_actors"].append(Actor.objects.get(pk=actor.actor_id))

        return context

class ActorListView(ListView):

    model = Actor
    template_name = "movies_app/actor_list.html"


class ActorDetailView(DetailView):

    model = Actor
    template_name = "movies_app/actor_detail.html"
    context_object_name = "actor"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # get all films in which this actor has worked
        films_of_this_actor = FilmActor.objects.filter(actor=context["actor"])
        context["all_films"] = []

        for film in films_of_this_actor:
            context["all_films"].append(Film.objects.get(pk=film.film_id))

        return context

