from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        label='Your name',
        label_suffix=' ',
        initial='Sonam',
        required=True,
        disabled=True,
        help_text='Limit 70 char',
    )
