from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=255, verbose_name='Токен')
