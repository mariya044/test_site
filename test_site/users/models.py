from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)

