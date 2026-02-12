from django.db import models

class User(models.Model):
    nameUser = models.CharField(("Name"), max_length=50) ##Campo --- tipo do campo
    emailUser = models.EmailField(('Email'))
    passwordUser = models.CharField(("Password"), max_length=8)

    def __str__(self):
        return self.nameUser
# Create your models here.
