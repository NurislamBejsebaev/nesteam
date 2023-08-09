from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.OneToOneField(
        to=User,
        blank=True,
        on_delete=models.CASCADE
    )
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
