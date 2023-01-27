from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Customer

"""
for info about how to use signals to create customer instances whenever a CustomUser is instantiated check:

https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

Also, check signals documentation at:

https://docs.djangoproject.com/en/3.2/topics/signals/
"""


@receiver(signal=post_save, sender=get_user_model(), dispatch_uid="create_customer")
def create_costumer(sender, instance, created, **kwargs):
    """
    Used to create a customer whenever a user is created.
    """

    if not instance.is_staff: # this is only for customers
        if created: # if a new user instance
            Customer.objects.create(personal_info=instance) # create a new customer based in the new user instance
