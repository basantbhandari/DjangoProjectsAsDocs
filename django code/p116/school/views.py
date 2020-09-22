from django.shortcuts import render
from school.forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


# Create your views here.
class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    initial = {
        'name': 'basant',
        'email': 'abc@gmail.com',
        'msg': 'write your thought',
    }
    success_url = '/thankyou/'

    def form_valid(self, form):
        print('************************************************')
        print(form)
        print('************************************************')
        print(form.cleaned_data['name'])
        print('************************************************')
        print(form.cleaned_data['email'])
        print('************************************************')
        print(form.cleaned_data['msg'])
        print('************************************************')
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = "school/thank.html"
