from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Sonam",
                           help_text='It can store only 30 letters')
