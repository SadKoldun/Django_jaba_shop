from django.urls import path, include
from carts import views

app_name = 'carts'

urlpatterns = [

    path('current_cart/', views.current_cart, name='current_cart'),
    path('add_cart/<int:product_id>', views.add_cart, name='add_cart'),
    path('change_cart/<int:product_id>', views.change_cart, name='change_cart'),
    path('del_cart/<int:cart_id>', views.del_cart, name='del_cart'),

]