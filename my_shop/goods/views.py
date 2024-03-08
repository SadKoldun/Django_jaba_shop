from django.shortcuts import render, get_list_or_404, redirect
from goods.models import Category, Product, Comment
from django.core.paginator import Paginator
# Create your views here.
from goods.utils import q_search
from goods.forms import CommentForm
from .models import Product


def catalog(request, cat_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if cat_slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=cat_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, per_page=8)
    current_page = paginator.get_page(page)
    context = {
        'goods': current_page,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Comment.objects.create(
                user=request.user,
                product=product,
                rating=comment_form.cleaned_data['rating'],
                comment_text=comment_form.cleaned_data['comment_text']

            )

            rate = comments.product_rate()
            product.rate = rate
            product.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        comment_form = CommentForm()

    context = {
        'product': product,
        'form': comment_form,
        'comments': comments,
    }
    return render(request, 'goods/product.html', context)
