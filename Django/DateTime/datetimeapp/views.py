from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def showdatetime(r):
    time = datetime.datetime.now().time()
    # datetime.datetime.now has first 10 index for date(including spaces)
    # So here we just sliced it to get only time up to second - str(datetime.datetime.now())[0:8]

    date = datetime.date.today().strftime('%A, %B %d, %Y')
    # %A - For Day_Name
    # %B - For Month_name
    # %d - For Date
    # %Y - Year

    return HttpResponse("<h1>Server Date is :: "+str(date)+"\n Server Time is :: "+str(time)[0:8]+"</h1>")
