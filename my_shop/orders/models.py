from django.db import models

# Create your models here.
from goods.models import Product
from users.models import User


class OrderedItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(order.product_price() for order in self)

    def total_quantity(self):
        if self:
            return sum(order.quantity for order in self)
        return 0


class Order(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='Пользователь', default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    delivery = models.BooleanField(default=False, verbose_name='Доставка')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при получении')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='Обработка', verbose_name='Статус заказа')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'№ {self.pk} | {self.user.first_name} {self.user.first_name}'


class OrderedItem(models.Model):

    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(to=Product, on_delete=models.SET_DEFAULT, null=True, verbose_name='Товар', default=None)
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')

    class Meta:
        db_table = 'ordered_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    objects = OrderedItemQuerySet.as_manager()

    def product_price(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f"{self.name} | {self.order.pk}"