from django.db import models

# Create your models here.
class Categories(models.Model):
    cid = models.CharField(max_length=15)
    cname = models.CharField(max_length=50)

class Product(models.Model):
    pid = models.CharField(max_length=15)
    pname = models.CharField(max_length=50)
    prize = models.CharField(max_length=15)
