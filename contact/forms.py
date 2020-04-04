from django import forms
from contact.models import EnrollForDemo

class EnrollForDemoForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Enter Last Name'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Enter Father\'s Name'}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Enter Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Enter Email'}))
    student = forms.ChoiceField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item', 'placeholder': 'Choose the Type of Registration'}))
    class Meta:
        model = EnrollForDemo
        fields = ['first_name', 'last_name', 'father_name', 'email', 'mobile_number', 'student']