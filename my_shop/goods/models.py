from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id', )

    def get_absolute_url(self):
        return reverse('goods:product', kwargs={'product_slug':self.slug})

    def __str__(self):
        return f'Товар {self.name} | Количество: {self.quantity}'

    def sell_price(self):

        return round(self.price - self.price * self.discount / 100, 2)
