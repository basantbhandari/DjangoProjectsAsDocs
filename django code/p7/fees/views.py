from django.shortcuts import render

# Create your views here.


def fee_python(request):
    return render(request, 'feespython.html')


def fee_django(request):
    return render(request, 'feesdjango.html')