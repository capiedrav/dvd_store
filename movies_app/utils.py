import os
from django.conf import settings
from bing_image_downloader import downloader
from movies_app.models import Film, Actor

"""
Run these functions from the Django shell: 
python manage.py shell
"""


def get_film_posters_from_internet():

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
