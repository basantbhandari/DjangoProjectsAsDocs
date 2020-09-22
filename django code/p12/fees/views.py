from django.shortcuts import render

# Create your views here.


def fee_course(request):
    return render(request, 'fees/fees.html')
