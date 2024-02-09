from goods.models import Product
from carts.models import Cart

from django.shortcuts import render, redirect


def current_cart(request):
    context = {}
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user)
        if carts.exists():
            context = {
                "carts": carts,
            }
    return render(request, 'carts/main_cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def change_cart(request, product_id):
    pass


def del_cart(request, product_id):
    pass
