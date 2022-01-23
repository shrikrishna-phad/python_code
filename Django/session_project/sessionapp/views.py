from django.shortcuts import render

# Create your views here.

def get_name(request):
    return render(request,'sessionapp/name.html')

def get_income(request):
    name = request.GET['name']
    responce = render(request,'sessionapp/income.html')

    responce.set_cookie('name',name)
    return responce

def get_bonus(request):
    #name = request.COOKIES['name']
    income = request.GET['income']

    responce = render(request,'sessionapp/bonus.html')

    responce.set_cookie('income',income)

    return responce

def get_result(request):
    name = request.COOKIES['name']
    income = request.COOKIES['income']
    bonus = request.GET['bonus']
    result = int(income)+(int(income)*int(bonus)/100)

    responce = render(request,'sessionapp/result.html',{'name':name,'income':income,'bonus':bonus,'result':result})

    responce.set_cookie('bonus',bonus)

    return responce
