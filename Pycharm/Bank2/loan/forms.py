from django import forms
from .models import Loan

class HomeLoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        exclude = ['car_brand','car_model','type_business','city_business','condition']

class BusinessLoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        exclude = ['car_brand','car_model','city_home','address_home','condition']

class CarLoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        exclude = ['city_home','address_home','type_business','city_business']