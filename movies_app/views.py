from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Film, Actor, FilmActor
from store_app.models import Inventory, Customer


# Create your views here.
class FilmListView(ListView):

    model = Film
    template_name = "movies_app/film_list.html"
    paginate_by = 50 # display 50 items at a time
    queryset = Film.objects.select_related("filmcategory").all().order_by("title")


class FilmDetailView(DetailView):

    model = Film
    template_name = "movies_app/film_detail.html"
    context_object_name = "film"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        film_actors = FilmActor.objects.filter(film=context["film"]).prefetch_related("actor")
        context["all_actors"] = []

        for film_actor in film_actors:
            context["all_actors"].append(film_actor.actor)

        # get five films to suggest to the user
        context["suggested_films"] = Film.objects.select_related("filmcategory").exclude(
            title=context["film"].title)[:5]

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
    queryset = Actor.objects.all().order_by("last_name", "first_name")


class ActorDetailView(DetailView):

    model = Actor
    template_name = "movies_app/actor_detail.html"
    context_object_name = "actor"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # get all films in which this actor has worked
        films_of_this_actor = FilmActor.objects.prefetch_related("film").filter(actor=context["actor"]).\
            order_by("film__title")

        context["all_films"] = []

        for film in films_of_this_actor:
            context["all_films"].append(film.film)

        # get five more actors to show
        context["more_actors"] = Actor.objects.exclude(actor_uuid=context["actor"].actor_uuid)[:5]

        return context
