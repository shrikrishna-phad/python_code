from django.db import models

# Create your models here.

gender_choices=(
    ("M","Male"),
    ("F","Female")
)

stream_choices=(
    ("Mech","Mechanical"),
    ("IT","Information & Technology"),
    ("CSE","Computer Science"),
    ("EnT","Electronics & Telecommunication")
)


class StudentModel(models.Model):
    stu_id = models.IntegerField(unique=True)
    stu_name = models.CharField(max_length=50)
    stu_gender = models.CharField(choices=gender_choices,max_length=2)
    stu_stream = models.CharField(choices=stream_choices,max_length=5)
    stu_avgmarks = models.FloatField()