from django.contrib import admin
from goods.models import Category, Product, Comment

# Register your models here.
# admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'comment_text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'quantity', 'discount']
    list_editable = ['price', 'quantity', 'discount']
    search_fields = ['name']
    fields = ['name', 'category', 'slug', ('price', 'discount'), 'quantity', 'image', 'description']


