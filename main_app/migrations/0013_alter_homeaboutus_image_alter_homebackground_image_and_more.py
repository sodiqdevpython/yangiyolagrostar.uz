# Generated by Django 4.2 on 2025-05-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeaboutus',
            name='image',
            field=models.ImageField(upload_to='about-us', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='homebackground',
            name='image',
            field=models.ImageField(upload_to='backgrounds', verbose_name='Orqa fon rasmi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Yangilik rasmi'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='image',
            field=models.ImageField(upload_to='employe', verbose_name='Xodimning rasmi'),
        ),
    ]
