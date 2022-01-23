from django.shortcuts import render
from .forms import EmployeeForms
from .forms import YesNo
# Create your views here.


def thanks(request,data):
    return render(request,'modelformsapp/thanks.html',context=data)


def showform(request):
    form = EmployeeForms
    md = {'form':form}
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save(commit=True) # To save the data in database
            print('form.cleaned_data',form.cleaned_data)
            return thanks(request,form.cleaned_data)

            #return thanks(request,form.cleaned_data)

    return render(request,'modelformsapp/form.html',context=md)