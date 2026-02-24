from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    #interest = models.CharField(("interest"), max_length=200)

#    def __str__(self):
#       return self.nameUser
# Create your models here.
