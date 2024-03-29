from django.db import models

# Create your models here.
class Seller(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()

class Buyer(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()

class Delivery(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    