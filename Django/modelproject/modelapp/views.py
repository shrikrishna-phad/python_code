from django.shortcuts import render
from .models import Student
# Create your views here.

def studentdata(request):
    stu_list = Student.objects.all()
    md = {'stu_list':stu_list}

    return render(request,'modelapp/student.html',context=md)