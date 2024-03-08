from django.contrib import admin
from carts.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_timestamp']
    search_fields = ['user', 'product', 'created_timestamp']


class UserCartsAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1
