from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL', default=None, null=False)

    def __str__(self):
        return self.name
