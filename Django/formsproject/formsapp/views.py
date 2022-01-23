from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

def showdata(request):
    form = FeedbackForm()
    md = {'form': form}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            return render(request,'formsapp/thanks.html',context=data)
            #thanks(request)

    return render(request,'formsapp/feedback.html',context=md)


def thanks(request):
    form = FeedbackForm(request.POST)
    data = form.cleaned_data
    #data = showdata.data
    #data = dict(data)
    #data = {'data':data}
    return render(request,'formsapp/thanks.html',context=data)