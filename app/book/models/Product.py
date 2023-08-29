from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', db_index=True)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField( verbose_name='Цена')
    photo = models.ImageField(upload_to="book-photo/", verbose_name='Фото', null=True)
    sale = models.IntegerField(default=0, verbose_name='Скидка %')
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    count_product = models.IntegerField(default=0, verbose_name='Количество в наличие')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', default=None, null=False)

    def __str__(self):
        return self.name



