from django import forms

from enroll.models import User


class UserForm(forms.ModelForm):
    """Form definition for User."""
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('student_name', 'email', 'password')


class TeacherForm(UserForm):
    """Form definition for TeacherForm."""
    class Meta:
        """Meta definition for TeacherForm."""

        model = User
        fields = ('teacher_name', 'email', 'password')
