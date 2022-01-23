from django import forms
from .models import EmployeeModel

# create your forms here.

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
