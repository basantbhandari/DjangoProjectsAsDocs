from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valpwd = cleaned_data['password']
        valrpwd = cleaned_data['rpassword']
        if valpwd != valrpwd:
            raise forms.ValidationError('Password Not Matched')
