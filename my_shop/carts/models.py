from django.core.validators import MinValueValidator
from django.db import models
from users.models import User
from goods.models import Product


class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Количество')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['-created_timestamp']

    objects = CartQuerySet.as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'{self.user.username} | {self.product.name} | Количество: {self.quantity}'
        return f'Без аутентификации | {self.product.name} | Количество: {self.quantity}'
