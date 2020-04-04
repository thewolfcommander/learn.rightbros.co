from django import forms
from contact.models import EnrollForDemo

class EnrollForDemoForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.(attrs={'class': 'form-control', 'class': 'item'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item'}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'class': 'item'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'class': 'item'}))
    student = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'class': 'item'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'class': 'item'}))
    class Meta:
        model = EnrollForDemo
        fields = ['first_name', 'last_name', 'father_name', 'email', 'mobile_number', 'student', 'about']