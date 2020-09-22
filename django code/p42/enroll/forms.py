from django import forms


class StudentRegistration(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(error_messages={'required': 'Enter your name here'})
    email = forms.EmailField(
        error_messages={'required': 'Enter your email here'},
        min_length=5,
        max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'required': 'Enter your password here'},
        min_length=5,
        max_length=50)
