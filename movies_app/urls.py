from django.urls import path, re_path
from .views import FilmListView, FilmsByCategoryListView,\
    ActorListView, FilmDetailView, ActorDetailView

# regex for filtering film categories urls
categories_re_url = r"^(?P<film_category>action|animation|children|classics|comedy|documentary|drama|family|foreign" \
                    r"|games|horror|music|new|sci-fi|sports|travel)_films/$"

urlpatterns = [
    path("films/", FilmListView.as_view(), name="film_list"),
    # note the use of re_path to filter urls using regex
    re_path(categories_re_url, FilmsByCategoryListView.as_view(), name="films_by_category"),
    path("films/<uuid:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("actors/", ActorListView.as_view(), name="actor_list"),
    path("actors/<uuid:pk>/", ActorDetailView.as_view(), name="actor_detail"),

]
