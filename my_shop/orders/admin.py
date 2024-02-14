from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderedItem


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderedItem
    fields = 'product', 'name', 'price', 'quantity'
    extra = 0


@admin.register(OrderedItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = 'order', 'product', 'name', 'price', 'quantity'


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp'

    readonly_fields = ('created_timestamp',)
    inlines = (OrderItemTabularAdmin,)
