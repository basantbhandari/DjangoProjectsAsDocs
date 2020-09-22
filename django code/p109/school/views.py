from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.


class BootstrapJumboTronRedirect(RedirectView):
    url = 'https://getbootstrap.com/docs/4.5/components/jumbotron/'


class RedirectToHome(RedirectView):
    url = '/'
