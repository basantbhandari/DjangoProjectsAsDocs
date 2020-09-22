from django import forms
from enroll.models import User


class UserForm(forms.ModelForm):
    """Form definition for User."""
    class Meta:
        """Meta definition for Userform."""

        model = User
        # fields = ('name', 'password', 'email')
        # fields = '__all__'
        exclude = ('name', 'password')
