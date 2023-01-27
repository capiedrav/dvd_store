from django.template import Library
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

        length_formatted = f"{hours}h:{minutes}m"

    return length_formatted
