from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import Group
from web_base.decorators import unauthenticated_user, allowed_users
from .forms import MyUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.conf import settings



# Create your views here.

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='student' or 'customer' or 'instructor')
            user.groups.add(group)
            
            messages.success(request, f'Account successfully created for {username}! You can now login.')
            return redirect('login')
    else:
        form = MyUserCreationForm()
    return render(request, 'web_users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account successfully updated!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'web_users/profile.html', context)

@unauthenticated_user
def loginPage(request):
    page = 'login'
    
    #if request.user.is_authenticated:
    #    return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            User = settings.AUTH_USER_MODEL
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username OR password does not exist')
            
    context = {'page': page}
    return render(request, 'web_users/login.html', context)

def logoutUser(request):
    
    return redirect('logout')

def passwordReset(request):
    return render(request, 'web_users/password_reset.html')