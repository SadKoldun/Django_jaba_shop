from statistics import mean

from django.db import models

from django.urls import reverse

from users.models import User


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
    rate = models.FloatField(default=0, verbose_name='Оценка')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('id', )

    def get_absolute_url(self):
        return reverse('goods:product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return f'Товар {self.name} | Количество: {self.quantity}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        else:
            return self.price


class CommentQuerySet(models.QuerySet):

    def product_rate(self):
        if self:
            return mean(comment.rating for comment in self if comment.rating != 0)
        return 0


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, verbose_name='Товар', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(verbose_name='Оценка', default=0)
    comment_text = models.TextField(max_length=300, verbose_name='Текст комментария')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    objects = CommentQuerySet.as_manager()

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_timestamp']

    def __str__(self):
        return f'{self.user.username} | {self.comment_text[:30]} | {self.created_timestamp}'
