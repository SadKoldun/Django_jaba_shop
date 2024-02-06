from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('main:index')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect('main:index')

    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)
