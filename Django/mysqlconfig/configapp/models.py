from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    mobile = models.IntegerField()
