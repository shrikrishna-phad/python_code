from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def show(request):
    return HttpResponse("<h1>Welcome to urlapptest</h1>")

def display(request):
    return HttpResponse('<h1> This is an Error </h1>')

def show1(request):
    return HttpResponse("""<h1>Django is Eating my BRAIN</h1>""")

