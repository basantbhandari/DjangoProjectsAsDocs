from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from enroll.forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created successfully !!!')
            user = fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
            return HttpResponseRedirect('/profile/')
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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile Updated !!!')
                fm.save()

        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {
            'name': request.user.username,
            'form': fm,
            'users': users
        })
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


# user details
def user_details(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, 'enroll/userdetails.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')
