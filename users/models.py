from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    interest = models.CharField(("interest"), max_length=200)

