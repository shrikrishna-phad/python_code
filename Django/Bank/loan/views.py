from django.shortcuts import render
from .forms import HomeLoanForm, BusinessLoanForm, CarLoanForm
import random

# Create your views here.


def ref_no():
    ref_no = random.randint(999999999,10000000000)
    return ref_no


def Hthanks(request,ref_no):
    return render(request,'loan/Hthanks.html',{'ref_no':ref_no})


def baseloan(request):
    return render(request,'loan/loan.html')


def homeloanshow(request):
    Hform = HomeLoanForm()
    hmd = {'Hform': Hform}
    if request.method == "POST":
        # populate form with data received from template
        Hform = HomeLoanForm(request.POST, request.FILES)

        # check whether the data is valid
        if Hform.is_valid():

            # cleaned.data pre-defined dictionary of data received
            Hform.cleaned_data['ref_id'] = ref_no()

            # Save data into database
            Hform.save(commit=True)

            # go to thanks page
            return Hthanks(request,Hform.cleaned_data['ref_id'])

        else:
            form = HomeLoanForm()
            print('form ::: ',form)

    return render(request,'loan/homeloan.html',context=hmd)

def carloanshow(request):
    Cform = CarLoanForm()
    cmd = {'Cform':Cform}
    if request.method == 'POST':
        Cform = CarLoanForm(request.POST)

        if Cform.is_valid():

            Cform.cleaned_data['ref_id'] = ref_no()
            Cform.save()

            return Hthanks(request,Cform.cleaned_data['ref_id'])

    return render(request,'loan/carloan.html',context=cmd)


def businessloanshow(request):
    Bform = BusinessLoanForm()
    bmd = {'Bform':Bform}
    if request.method == 'POST':
        Bform = BusinessLoanForm(request.POST)

        if Bform.is_valid():

            Bform.cleaned_data['ref_id'] = ref_no()
            Bform.save()

            return Hthanks(request,Bform.cleaned_data['ref_id'])

    return render(request,'loan/businessloan.html',context=bmd)
