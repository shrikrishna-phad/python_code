from django.shortcuts import render
from .models import Employee
# Create your views here.


def display(request):
    emp_list = Employee.objects.all()
    md = {'emp_list':emp_list}

    return render(request,'d2htmlapp/Employee.html',context=md)