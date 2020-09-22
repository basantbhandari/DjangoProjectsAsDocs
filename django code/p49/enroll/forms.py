from django import forms
from django.core import validators
from enroll.models import StudentRegistration


class StudentRegistrationForm(forms.ModelForm):
    """Form definition for StudentRegistration."""
    class Meta:
        """Meta definition for StudentRegistrationform."""

        model = StudentRegistration
        fields = ('name', 'email', 'password')
        widgets = {
            'name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'email':
            forms.EmailInput(attrs={'class': 'form-control'}),
            'password':
            forms.PasswordInput(render_value=True,
                                attrs={'class': 'form-control'}),
        }
