# Generated by Django 4.2.3 on 2023-07-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='dd', max_length=255, verbose_name='URL'),
        ),
    ]