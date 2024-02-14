from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderedItem
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return redirect('main:index')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return redirect('main:index')

    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, f'Изменения профиля успешно сохранены')
            return redirect(reverse('users:profile'))
    else:
        profile_form = UserProfileForm(instance=request.user)

    # orders = Order.objects.filter(user=request.user).prefetch_related(
    #      Prefetch(
    #          "ordereditem_set",
    #          queryset=OrderedItem.objects.select_related("product"),
    #      )
    # ).order_by("-id")

    orders = Order.objects.filter(user=request.user).order_by("-id")
    context = {
        "form": profile_form,
        "orders": orders,

    }
    return render(request, 'users/profile.html', context)
