from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('login')
    else:
        register_form = forms.RegistrationForm()
    return render(request,'register.html',{'form':register_form,'type':'Register'})


def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,data = request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in Successfully')
                login(request,user)
                return redirect('profile')
            else:
                messages.warning(request,'Account Information Incorrect')
                return redirect('signup')
    else:
        login_form = AuthenticationForm()
    return render(request,'register.html',{'form':login_form,'type':'Login'})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request,'profile.html',{'data':data})

@login_required
def edit_profiles(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST,instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request,'update_profile.html',{'form':profile_form})

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def change_pass(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def read_post(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'profile.html', {'post': post})
