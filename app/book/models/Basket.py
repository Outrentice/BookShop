from django.db import models
from django.contrib.auth.models import User


class Basket(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Книга')
    count_product = models.IntegerField(default=1, verbose_name='Количество товара в корзине')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.user} - {self.product}'
