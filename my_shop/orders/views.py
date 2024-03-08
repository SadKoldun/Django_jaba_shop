from django.contrib import messages
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from orders.forms import CreateOrderForm
from django.db import transaction
from carts.models import Cart
from orders.models import Order, OrderedItem


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            delivery=form.cleaned_data['delivery'],
                            address=form.cleaned_data['address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточное количество товара {name} на складе\
                                                              В наличии - {product.quantity}')

                            OrderedItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()

                        cart_items.delete()

                        return redirect('users:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('carts:order')

    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)
    context = {
        'form': form,
    }
    return render(request, 'orders/create_order.html', context)
