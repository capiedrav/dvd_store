from django.views.generic import TemplateView
from movies_app.models import FilmCategory


# Create your views here.
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # to avoid querying the database, hardcode the ids for each category in the category table
        ACTION = 1
        COMEDY = 2
        DRAMA = 3

        featured_films = []
        for category in [ACTION, COMEDY, DRAMA]: # get two films for each category
            for film_and_category in FilmCategory.objects.filter(category=category)[:2]:
                featured_films.append(film_and_category)

        context["featured_films"] = featured_films

        return context


class AboutPageView(TemplateView):

    template_name = "about.html"
