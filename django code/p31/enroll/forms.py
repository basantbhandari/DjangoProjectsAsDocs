from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'somecss1',
        'id': 'unique_id'
    }))
