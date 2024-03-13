from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'product_api'


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('products/', views.ProductViewSet.as_view()),

]


