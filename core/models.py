from statistics import mode
from django.db import models

class CloudFunctions(models.Model):
    title = models.CharField(max_length=55)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title

class Options(models.Model):
    panel = models.CharField(max_length=55)
    hdd = models.IntegerField()
    data = models.IntegerField()
    support = models.CharField(max_length=55)
    theme = models.CharField(max_length=55)

    def __str__(self) -> str:
        return self.panel



class HostProduct(models.Model):
    name = models.CharField(max_length=55)
    price = models.CharField(max_length=20)
    desc = models.TextField()
    settings = models.ForeignKey(Options, on_delete=models.CASCADE, related_name='related_hdd')
    

    def __str__(self) -> str:
        return self.name
    

class AboutUs(models.Model):
    name = models.CharField(max_length=266)
    text = models.TextField()
    profession = models.CharField(max_length=266)

    