from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    Employee_id = models.IntegerField()
    Employee_Name = models.CharField(max_length=100)
    Employee_Salary = models.IntegerField()
    Employee_Address = models.CharField(max_length=225)
    Date = models.DateField(auto_now_add=True)
    Date_Time = models.DateTimeField(auto_now_add=True)