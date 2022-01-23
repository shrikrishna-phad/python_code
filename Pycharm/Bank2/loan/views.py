from django.shortcuts import render
from .forms import HomeLoanForm,BusinessLoanForm,CarLoanForm
import random

# Create your views here.


def Hthanks(request):
    ref_no = random.randint(999999999, 9999999999)
    return render(request,'loan/Hthanks.html',{'ref_no':ref_no})


def baseloan(request):
    return render(request,'loan/loan.html')


def homeloanshow(request):
    form = HomeLoanForm()
    md = {'form':form}
    if request.method == 'POST':
        form = HomeLoanForm(request.POST)
        if form.is_valid():
            form.save()
            return Hthanks(request)

    return render(request,'loan/homeloan.html',context=md)

