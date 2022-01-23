from django.contrib import admin
from .models import EmployeeModel,EmployeeModel2

# Register your models here.

@admin.register(EmployeeModel,EmployeeModel2)
class EmployeeAdmin(admin.ModelAdmin):
    #list_display = ['E_id','E_Name','E_Address','E_Mobile']
    pass


#class EmployeeAdmin2(admin.ModelAdmin):
    #list_display = ['E_id','E_Salary','E_Position','E_Department']
#    pass

#models = [EmployeeModel,EmployeeModel2]
#admin.site.register(models,EmployeeAdmin)

#admin.site.register(EmployeeModel2,EmployeeAdmin)
