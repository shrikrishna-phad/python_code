from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel
from django.http import HttpResponse
# Create your views here.


def show(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Thanks For Filling The Form </h1>")
    return render(request,'ormapp/show.html',{'form': form})


def emp_show(request):
    # To show all data
    form = StudentModel.objects.all()

    # To show id > 104
    form1 = StudentModel.objects.filter(stu_id__gt=104)

    # To show id >= 104
    form2 = StudentModel.objects.filter(stu_id__gte=104)

    # To show id < 104
    form3 = StudentModel.objects.filter(stu_id__lt=104)

    # To show id <= 104
    form4 = StudentModel.objects.filter(stu_id__lte=104)

    # To show id in {104,106,101}
    form5 = StudentModel.objects.filter(stu_id__in=(104,106,101))

    # To show name == radhika
    form6 = StudentModel.objects.filter(stu_name__exact='radhika')

    # To show name == radhika
    form7 = StudentModel.objects.filter(stu_name__iexact='radhika')

    # To show name == contains ra case sensitive
    form8 = StudentModel.objects.filter(stu_name__contains='ra')

    # To show name == contains ra case insensitive
    form9 = StudentModel.objects.filter(stu_name__icontains='ra')

    # To show name starting with == r case sensitive
    form10 = StudentModel.objects.filter(stu_name__startswith='r')

    # To show name starting with == r case insensitive
    form11 = StudentModel.objects.filter(stu_name__istartswith='r')

# ----------------------------------------------------------------------------------------------------------------------

    # Combining Two Queries
        # METHOD 1
    q1 = StudentModel.objects.filter(stu_name__istartswith='r')
    q2 = StudentModel.objects.filter(stu_gender__iexact='m')

    form12 = StudentModel.objects.filter(stu_name__istartswith='r') | StudentModel.objects.filter(stu_gender__iexact='m')

    form13 = StudentModel.objects.filter(stu_name__istartswith='r') | StudentModel.objects.filter(stu_gender__iexact='m')

    form12 = q1 | q2  # or
    form13 = q1 & q2  # and

    # Combining Two Queries
        # METHOD 2
    from django.db.models import Q

    form14 = StudentModel.objects.filter(Q(stu_name__istartswith='r') | Q(stu_gender__iexact='m'))

    form15 = StudentModel.objects.filter(Q(stu_name__istartswith='r') & Q(stu_gender__iexact='m'))

    # Aggregate functions
    from django.db.models import Avg,Sum,Max,Min,Count

    form16 = StudentModel.objects.all().aggregate(Avg('stu_avgmarks'))

    form17 = StudentModel.objects.all().aggregate(Sum('stu_avgmarks'))

    form18 = StudentModel.objects.all().aggregate(Min('stu_avgmarks'))

    form19 = StudentModel.objects.all().aggregate(Max('stu_avgmarks'))

    form20 = StudentModel.objects.all().aggregate(Count('stu_avgmarks'))

    return render(request,'ormapp/emp.html',{'form':form,'form1':form1,'form2':form2,'form3':form3,'form4':form4,
                                             'form5':form5,'form6':form6,'form7':form7,'form8':form8,'form9':form9,
                                             'form10':form10,'form11':form11,'form12':form12,'form13':form13,
                                             'form14':form14,'form15':form15,'form16':form16,'form17':form17,
                                             'form18':form18,'form19':form19,'form20':form20})