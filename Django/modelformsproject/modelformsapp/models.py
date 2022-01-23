from django.db import models

# Create your models here.

class Employee(models.Model):
    idd = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    mobile = models.BigIntegerField()

