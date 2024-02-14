from django import template

from orders.models import OrderedItem

register = template.Library()


@register.simple_tag()
def in_order_items(order):

    return OrderedItem.objects.filter(order=order.id)


