from django.http import JsonResponse
from django.template.loader import render_to_string

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

    get_cart = get_user_carts(request)

    cart_html = render_to_string(
        "carts/main_cart.html",
        {"carts": get_cart},
        request=request)

    return JsonResponse({'cart_html': cart_html})


# def change_cart(request):
#     cart_id = request.POST.get('cart_id')
#     quantity = request.POST.get('quantity')
#
#     cart = Cart.objects.get(id=cart_id)
#
#     cart.quantity = quantity
#     cart.save()
#     new_quantity = cart.quantity
#
#     get_cart = get_user_carts(request)
#
#     cart_html = render_to_string(
#         "carts/main_cart.html",
#         {"carts": get_cart},
#         request=request)
#
#     response_data = {
#         'cart_html': cart_html,
#         'quantity': new_quantity,
#     }
#
#     return JsonResponse(response_data)


def del_cart(request):

    cart_id = request.POST.get('cart_id')
    cart = Cart.objects.get(id=cart_id)

    quantity = cart.quantity
    cart.delete()

    user_cart = get_user_carts(request)
    cart_html = render_to_string(
        "carts/main_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "cart_html": cart_html,
        "quantity_deleted": quantity,
    }

    return JsonResponse(response_data)
