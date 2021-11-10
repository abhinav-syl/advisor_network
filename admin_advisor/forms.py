from django import forms

class advisor_form(forms.Form):
    name = forms.CharField(label = "name",max_length=100)
    
    url = forms.CharField(label = "url",max_length=100)