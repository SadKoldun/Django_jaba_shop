from django.urls import path, include
from carts import views

app_name = 'carts'

urlpatterns = [

    path('add_cart/', views.add_cart, name='add_cart'),
    path('change_cart/', views.change_cart, name='change_cart'),
    path('del_cart/', views.del_cart, name='del_cart'),

]
