from django.contrib import admin
from .models import CustomAdminModel, Query
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display = ['employee_id','username','query1','isexicuted',]

class QueryAdmin(admin.ModelAdmin):
    list_display = ['query2']

admin.site.register(CustomAdminModel,CustomAdmin)
admin.site.register(Query,QueryAdmin)
