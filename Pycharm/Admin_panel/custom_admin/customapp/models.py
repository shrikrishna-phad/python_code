from django.db import models

# Create your models here.

class CustomAdminModel(models.Model):
    employee_id = models.IntegerField()
    username = models.CharField(max_length=25)
    query1 = models.TextField(help_text='Write your Query here')
    isexicuted = models.CharField(default='False',editable=False,max_length=10)


class Query(CustomAdminModel,models.Model):
    query2 = models.query.QuerySet(query=CustomAdminModel.query1)