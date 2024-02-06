from django.urls import path, include
from goods import views

app_name = 'goods'

urlpatterns = [

        path('<slug:cat_slug>/', views.catalog, name='catalog'),
        path('product/<slug:product_slug>', views.product, name='product'),
        path('search/', views.product, name='search')

]