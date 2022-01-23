from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class AccountOpenModel(models.Model):
    First_Name = models.CharField(max_length=30)
    Middle_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Mobile_Number = PhoneNumberField(unique=True)
    Address = models.CharField(help_text='Street Number,Locality',max_length=20),models.CharField(max_length=20)