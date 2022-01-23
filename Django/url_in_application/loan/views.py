from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homeloan(r):
    return HttpResponse("<h1>Welcome to Loan Department</h1> This is Home loan")


def personalloan(r):
    return HttpResponse("<h1>Welcome to Loan Department</h1> This is Personal loan")


def carloan(r):
    return HttpResponse("<h1>Welcome to Loan Department</h1> This is Car loan")