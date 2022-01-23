from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=25)
    age = forms.IntegerField()
    address = forms.CharField(max_length=50)
    email = forms.EmailField()
    date = forms.DateInput()
