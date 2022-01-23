from django.shortcuts import render

# Create your views here.

def show(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count'])+1

    else:
        newcount = 1

    responce = render(request,'sessiontest/test.html',{'count':newcount})

    responce.set_cookie('count',newcount,max_age=30)

    return responce