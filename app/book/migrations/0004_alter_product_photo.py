# Generated by Django 4.2.3 on 2023-07-17 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='book-photo/', verbose_name='Фото'),
        ),
    ]
