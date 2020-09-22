from django import forms


class StudentRegistration(forms.Form):
    #name = forms.CharField(min_length=5, max_length=10)
    #name = forms.CharField(strip=False)
    name = forms.CharField(
        error_messages={'required': 'Enter your value field'})

    agree = forms.BooleanField(label='i Agree')
    roll = forms.IntegerField(min_value=10, max_value=20)
    price = forms.DecimalField(max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=10, max_value=1000)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=10)
    website = forms.URLField(min_length=5, max_length=10)
    password = forms.CharField(min_length=5,
                               max_length=10,
                               widget=forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'somecss1 somecss2'}))
    notes = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'cols': 50
    }))

    agree = forms.BooleanField(label_suffix='', label='I agree')
