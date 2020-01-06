from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

#first we can import registration admin form

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

from django.contrib.auth import views as auth_views

def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(request.body)
        if form is not None and form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created {username}, you can log in')
            return redirect('users:login')
    else:
        form = UserRegistrationForm(label_suffix="")
    
    context = {
        'title':'User register form',
        'registration_form':form,
    }
    return render(request,'users/register.html', context)

@login_required
def profile(request):
    context = {
        'title':'User profile',
    }
    return render(request,'users/profile.html', context)
