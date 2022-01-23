from django.shortcuts import render
from .forms import EmployeeForm
from .models import EmployeeModel
from django.shortcuts import redirect
# Create your views here.


def show_data(request):
    employee = EmployeeModel.objects.all()

    return render(request,'curdapp/data_all.html',{'employee':employee})


def create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')

    return render(request,'curdapp/create.html',{'form':form})


def delete(request,id):
    employee = EmployeeModel.objects.get(id=id)
    employee.delete()

    return redirect('/')


def update(request,id):
    employee = EmployeeModel.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'curdapp/update.html',{'employee':employee})