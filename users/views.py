from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

#first we can import registration admin form

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfieUpdateForm

from django.contrib.auth import views as auth_views

from django.http import HttpResponse

def empty_view(request):
    return HttpResponse('')

def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form is not None and form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created {username}, you can log in')
            return redirect('profiles:login')
    else:
        form = UserRegistrationForm(label_suffix="")
    
    context = {
        'title':'User register form',
        'registration_form':form,
    }
    return render(request,'users/register.html', context)

@login_required
def profile(request):

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfieUpdateForm(instance=request.user.profile)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfieUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile,
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        username = u_form.cleaned_data.get('username')
        messages.success(request,f'{username} - your account updated')
        return redirect('profiles:profile')
    context = {
        'title':'User profile',
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html', context)
