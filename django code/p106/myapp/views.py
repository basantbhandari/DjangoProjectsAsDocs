from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post, Page, Song

# Create your views here.


def home(request):
    return render(request, 'myapp/home.html')


def user(request):
    data = User.objects.all()
    return render(request, 'myapp/user.html', {'students': data})


def page(request):
    data = Page.objects.all()
    return render(request, 'myapp/page.html', {'students': data})


def post(request):
    data = Post.objects.all()
    return render(request, 'myapp/post.html', {'students': data})


def song(request):
    data = Song.objects.all()
    print('********************************************')
    print(data)
    print('********************************************')
    return render(request, 'myapp/song.html', {'students': data})
