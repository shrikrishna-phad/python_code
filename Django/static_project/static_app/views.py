from django.shortcuts import render
import datetime
# Create your views here.

def BioData(request):
    Todays_Date = datetime.date.today()
    dob = datetime.date(1992,2,24)
    Age = Todays_Date-dob
    a = str(Age).split(' ')
    b = str(int(a[0])/365).split('.')[0]
    Personal_Details = {'firstname':'Shrikrishna','middlename':'Dattatraya','lastname':'Phad'}
    Additional_Details = {'gender':'Male','dob':dob,'age':{'int':b,'unit':'years'},'height':'163in',
                          'education':'Graduate(Engineering Mechanical)','city':'Pune'}
    Personal_Details['Additional_Details'] = Additional_Details

    return render(request,'static_app/biodata.html',context=Personal_Details)