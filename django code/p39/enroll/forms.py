from django import forms
from django.core import validators


def start_with_s(value):
    value = value.lower()
    if value[0] != 's':
        raise forms.ValidationError('Name should start with s')


class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[start_with_s])
    email = forms.EmailField()
