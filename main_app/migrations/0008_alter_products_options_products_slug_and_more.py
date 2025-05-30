# Generated by Django 5.2 on 2025-04-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Xizmat', 'verbose_name_plural': 'Xizmatlar'},
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='jcdxncij', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='media/products', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='Mahsulot'),
        ),
    ]
