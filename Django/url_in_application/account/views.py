from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def savingacc(r):

    return HttpResponse("<h1>Welcome to accounts department</h1> This is Savings account")


def savingadult(r):

    return HttpResponse("<h1>Welcome to accounts department</h1> This is Savings for adults account")


def savingminor(r):

    return HttpResponse("<h1>Welcome to accounts department</h1> This is Savings for minors account")


def currentacc(r):
    return HttpResponse("<h1>Welcome to accounts department</h1> This is Current account")