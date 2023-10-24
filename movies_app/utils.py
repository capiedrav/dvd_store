import os
from django.conf import settings
from bing_image_downloader import downloader
from movies_app.models import Film, Actor, FilmCategory


def get_film_posters_from_internet():
    """
    Run this function from the Django shell:
    python manage.py shell
    """

    films = Film.objects.all()
    output_dir = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/film_posters")

    for film in films: # iterate over all films
        # download images that correspond to film titles
        downloader.download(
            query=film.title,
            limit=1,
            output_dir=output_dir,
            adult_filter_off=False,
        )


def get_actor_images_from_internet():
    """
    Run this function from the Django shell:
    python manage.py shell
    """

    actors = Actor.objects.all()
    output_dir = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/actor_images")

    for actor in actors: # iterate over all actors
        # download images that correspond to actor names
        downloader.download(
            query=actor.first_name + " " + actor.last_name,
            limit=1,
            output_dir=output_dir,
            adult_filter_off=False,
            filter="photo"
        )


def remove_duplicate_actor_images():
    """
    Run this function from the Django shell:
    python manage.py shell
    """

    path = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/actor_images")

    actor_folders = os.listdir(path)

    for actor_folder in actor_folders:
        actor_path = os.path.join(path, actor_folder)
        actor_images = os.listdir(actor_path)
        number_of_images = len(actor_images)

        if number_of_images > 1:
            print(f"{number_of_images} images found at {actor_path}")
            image_to_remove = os.path.join(actor_path, actor_images[-1])
            print(f"Removing {image_to_remove}")
            os.remove(image_to_remove)


def get_films_by_category(category):
    """
    Retrieves all films in category. This function is used in FilmsByCategoryListView.

    :param category (string): film category
    :return: queryset of all films in category
    """

    films_in_category = FilmCategory.objects.select_related("film").filter(category__name=category).\
        order_by("film__title")

    return [film_in_category.film for film_in_category in films_in_category]
