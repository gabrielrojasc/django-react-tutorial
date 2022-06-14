# standard library
import random
import string

# django
from django.db import models


def generate_unique_code():
    length = 6
    choices = string.ascii_letters + string.digits
    while True:
        code = "".join(random.choices(choices, k=length))
        if not Room.objects.filter(code=code).exists():
            break
    return code


# Create your models here.
class Room(models.Model):
    """Model that represents a room"""

    code = models.CharField(
        max_length=8,
        default=generate_unique_code,
        unique=True,
    )
    host = models.CharField(
        max_length=50,
        unique=True,
    )
    guest_can_pause = models.BooleanField(
        null=False,
        default=False,
    )
    votes_to_skip = models.IntegerField(
        null=False,
        default=1,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
