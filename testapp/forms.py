from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']
        