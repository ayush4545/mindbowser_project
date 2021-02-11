from django.core import validators
from django import forms
from .models import employee,manager

class managerSignup(forms.ModelForm):
    
    class Meta:
        model = manager
        fields = ['email','fname','lname','password','address','dob','company']

class managerLogin(forms.ModelForm):
    class Meta:
        model=manager
        fields=['email','password']


class employeeUpdate(forms.ModelForm):
    class Meta:
        model=employee
        fields=['fname','lname','email','password','address','dob','company','mobile','city']  