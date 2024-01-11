from django.template import Library
from django.utils import timezone


register = Library()


@register.filter
def check_return_date(rental):
    """
    Check whether the return date of the DVD has expired, i.e., it's late.
    """

    return (not rental.inventory.available) and (timezone.now() > rental.return_date)


