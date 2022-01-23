from django.shortcuts import render

# Create your views here.

def tag1(request):
    dict1 = {'firstname': 'Shrikrishna','middlename':'Dattatraya','lastname':'Phad'}
    return render(request,'tagsapp/tag1.html',context=dict1)

def tag2(request):
    dict2 = {'firstname': 'Shrikrishna','middlename':'Dattatraya','lastname':'Phad'}
    dict3 = {'city':'Pune','gender':'Male','age':29}
    dict2['dict3'] = dict3
    return render(request,'tagsapp/tag2.html',context=dict2)
