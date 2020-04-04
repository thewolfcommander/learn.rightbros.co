from django import forms
from contact.models import EnrollForDemo

class EnrollForDemoForm(forms.ModelForm):
    class Meta:
        model = EnrollForDemo
        fields = ['first_name', 'last_name', 'father_name', 'email', 'mobile_number', 'student']