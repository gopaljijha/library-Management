from django import forms
from django.contrib.auth.models import User
from django.forms import CharField
from django.core import validators
from django.core.exceptions import ValidationError

from . import models

#Name = forms.CharField(validators =[validators.MaxLengthValidator(10)])
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30 )
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class AdminSigupForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs = {"placeholder": "FirstName"}))  # changes add here
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs = {"placeholder": "FirstName"}))  # changes add here
    username = forms.EmailField(widget=forms.TextInput(attrs = {"placeholder": "example@email.com"}))  # changes add here
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','password'] # changes  


# class AdminSigupForm(forms.ModelForm):
#     first_name = forms.CharField(label='', widget=forms.TextInput(attrs = {"placeholder": "first name"}))
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']

class StudentUserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs = {"placeholder": "first name"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs = {"placeholder": "first name"}))
    username = forms.EmailField(widget=forms.TextInput(attrs = {"placeholder": "example@email.com"}))  # changes add here
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    enrollment = forms.CharField(validators =[validators.MaxLengthValidator(10)], widget=forms.TextInput(attrs = {"placeholder": "Enter your Enrollment"}))
    branch = forms.CharField(widget=forms.TextInput(attrs = {"placeholder": "Enter your Branch"}))
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']
class IssuedBookForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')
    
