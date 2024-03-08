from django import template
from django.utils.http import urlencode

from goods.models import Category, Comment

register = template.Library()


@register.simple_tag()
def all_cats():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag()
def get_comment(request):
    return Comment.objects.filter(user=request.user).first()
