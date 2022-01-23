from django.contrib import admin
from .models import EmployeeModel

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Employee_id','Employee_Name','Employee_Salary','Employee_Address','Date','Date_Time']

admin.site.register(EmployeeModel,EmployeeAdmin)