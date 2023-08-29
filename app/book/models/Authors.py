from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя автора')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия автора', db_index=True)
    middle_name = models.CharField(max_length=255, verbose_name='Отчество автора')

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.middle_name) + ' ' + str(self.last_name)

