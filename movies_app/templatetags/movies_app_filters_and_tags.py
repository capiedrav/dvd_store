from django.template import Library
from django.template.defaultfilters import stringfilter
from django.conf import settings
import os

register = Library()


@register.filter
def format_film_length(value):
    """
    format the film length in minutes (int) to a string representing hours and minutes.
    """

    length_formatted = "N/A"
    if type(value) is int and value >= 0:
        hours = value // 60
        minutes = value % 60

        if hours:
            length_formatted = f"{hours}h:{minutes}m"
        else:
            length_formatted = f"{minutes}m"

    return length_formatted


@register.filter
@stringfilter
def path_to_image(image_name, film_poster=True):
    """
    Returns the path to the image.

    :param image_name: this can be a film name or an actor name
    :param film_poster: indicates whether the image is a film poster. If false, the image is of an actor
    :return: path to the image
    """

    image_path = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/")

    if film_poster:
        image_path += "film_posters/" + image_name + "/"
    else:
        image_path += "actor_images/" + image_name + "/"

    try:
        files = os.listdir(image_path)
    except FileNotFoundError:
        image_path = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/No-image-found.jpg")
    else:
        if len(files) == 1:
            image_path += files[0]
        else:
            image_path = os.path.join(settings.BASE_DIR, "movies_app/static/movies_app/images/No-image-found.jpg")

    return image_path.split("static/")[1] # return the relative path to the image
