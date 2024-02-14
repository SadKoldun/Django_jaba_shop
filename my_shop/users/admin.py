from django.contrib import admin

from carts.admin import UserCartsAdmin
from orders.admin import OrderTabularAdmin
from users.models import User


# Register your models here.
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']
    search_fields = ['username', 'first_name', 'last_name']

    inlines = [
        UserCartsAdmin, OrderTabularAdmin
    ]
