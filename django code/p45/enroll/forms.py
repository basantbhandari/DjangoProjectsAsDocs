from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Enter Name',
            'email': 'Enter Email',
            'password': 'Enter Password',
        }
        help_text = {'name': 'Enter Your Full Name'}
        error_messages = {
            'name': {
                'required': 'Name must be filled'
            },
            'email': {
                'required': 'Email must be filled'
            },
            'password': {
                'required': 'Password must be filled'
            }
        }

        widgets = {
            'password':
            forms.PasswordInput,
            'name':
            forms.TextInput(attrs={
                'class': 'myclass',
                'placeholder': 'your name here'
            })
        }
