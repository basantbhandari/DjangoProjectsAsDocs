from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from enroll.forms import SignUpForm

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created successfully !!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': fm})


# login form
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You are logged in')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()

        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


# Profile
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# Change password with old Password
def changepass_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                messages.success(request, 'Password changed successfully !!!')
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


# Change password without old Password
def changepass_view1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                messages.success(request, 'Password changed successfully !!!')
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
