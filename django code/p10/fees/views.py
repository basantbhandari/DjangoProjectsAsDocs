from django.shortcuts import render


# Create your views here.
def learn_one(request):
    return render(request, 'fees/feesone.html')


def learn_two(request):
    return render(request, 'fees/feestwo.html')
