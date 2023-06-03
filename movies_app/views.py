from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Film, Actor, FilmActor
from store_app.models import Inventory, Customer


# Create your views here.
class FilmListView(ListView):

    model = Film
    template_name = "movies_app/film_list.html"
    paginate_by = 50 # display 50 items at a time

    def get_queryset(self):
        # order films by title and retrieve their categories in a single query
        return Film.objects.select_related("filmcategory").all().order_by("title")


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

        # check whether the film is available for rental
        if self.request.user.is_authenticated:
            # get the customer trying to rent the film
            customer = get_object_or_404(Customer, personal_info=self.request.user)
            # a film is available for rental if it is available in the same store of the customer
            film_inventory = [film for film in Inventory.objects.filter(film=context["film"]) if film.available
                              and film.store == customer.store]
            context["film_availability"] = len(film_inventory) > 0

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

