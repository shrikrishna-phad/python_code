import random

from django.db import models

# Create your models here.
class Loan(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(help_text='In Years')
    address = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    loan_amount = models.IntegerField()
    loan_type= models.CharField(help_text="home/car/business",max_length=8)
    ref_id = models.BigIntegerField(null=True,blank=True)
    # for car loan
    condition = models.CharField(help_text="used/new",max_length=4)
    car_brand = models.CharField(max_length=10)
    car_model = models.CharField(max_length=10)
    # for home loan
    city_home = models.CharField(max_length=15)
    address_home = models.CharField(max_length=50)
    # for business loan
    type_business = models.CharField(max_length=10)
    city_business = models.CharField(max_length=15)