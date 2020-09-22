from django.shortcuts import render


# Create your views here.
def ProfileView(request):
    return render(request, 'registration/profile.html')