from django import forms

class register_form(forms.Form):
    name = forms.CharField(label = "name",max_length=100)
    
    email = forms.CharField(label = "email",max_length=100)
    
    password = forms.CharField(label = "password",max_length=100)
    
    
class login_form(forms.Form):
    
    email = forms.CharField(label = "email",max_length=100)
    
    password = forms.CharField(label = "password",max_length=100)
    
class book_form(forms.Form):
    booking_time = forms.CharField(label = "booking_time",max_length=20)