import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """
    User model for this project.
    """

    user_uuid = models.UUIDField(default=uuid.uuid4, editable=False, null=False, unique=True)
