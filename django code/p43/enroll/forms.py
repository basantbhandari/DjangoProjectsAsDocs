from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(error_messages={'required': 'Enter your name here'})
    email = forms.EmailField(
        error_messages={'required': 'Enter your email here'})
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Enter your password here'})
