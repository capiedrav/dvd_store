from django.views.generic import TemplateView
from movies_app.models import FilmCategory, Category


# Create your views here.
class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        film_categories = Category.objects.all() # get all film categories

        featured_films = []
        for category in film_categories: # for each film category
            # get two films for each category
            for film_category in FilmCategory.objects.select_related("film").filter(category=category)[:2]:
                featured_films.append(film_category)

        context["featured_films"] = featured_films
        context["film_categories"] = film_categories

        return context


class AboutPageView(TemplateView):

    template_name = "about.html"
