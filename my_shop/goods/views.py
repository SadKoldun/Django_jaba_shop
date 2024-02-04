from django.shortcuts import render
from goods.models import Category, Product
# Create your views here.


def catalog(request):
    goods = Product.objects.all()
    context = {
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)
