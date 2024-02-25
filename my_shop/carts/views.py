from goods.models import Product
from carts.models import Cart
from carts.utils import get_user_carts
from django.shortcuts import render, redirect


def current_cart(request):
    carts = get_user_carts(request)
    context = {
        'carts': carts
    }

    return render(request, 'carts/main_cart.html', context)


def add_cart(request):

    product_id = request.POST.get('product_id')
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
    else:
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def change_cart(request, product_id):
    pass


def del_cart(request, cart_id):
    Cart.objects.filter(id=cart_id).delete()
    return redirect(request.META['HTTP_REFERER'])
