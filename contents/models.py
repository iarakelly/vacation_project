from django.db import models

class Article(models.Model):
    titleArticle = models.CharField(("Name"), max_length=50) ##Campo --- tipo do campo
    summaryArticle = models.CharField(("Summary"), max_length=50)(('Summary'), max_length=500)
    sourceArticle = models.CharField(("Password"), max_length=50)

    def __str__(self):
        return self.titleArticle    ## retorna uma sting legivel pra cada objeto 
# Create your models here.
