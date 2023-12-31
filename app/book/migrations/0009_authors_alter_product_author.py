# Generated by Django 4.2.3 on 2023-07-18 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя автора')),
                ('last_name', models.CharField(db_index=True, max_length=255, verbose_name='Фамилия автора')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество автора')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.authors'),
        ),
    ]
