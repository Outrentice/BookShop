# Generated by Django 4.2.3 on 2023-07-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_product_price_product_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='user-photo/', verbose_name='Фото'),
        ),
    ]
