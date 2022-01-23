from django import forms
from .models import Employee


class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"  # To include all fields of model in form
        # fields = ('name','address') # To include only specified fields in form
        # exclude = ['name','address'] # To exclude only specified fields from the form

class YesNo(forms.Form):
    yes_no = forms.CharField(max_length=1)