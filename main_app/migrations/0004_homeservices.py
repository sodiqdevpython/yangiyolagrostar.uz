# Generated by Django 5.2 on 2025-04-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_delete_homeaboutfeatures'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=64, verbose_name='Class nomi')),
                ('title', models.CharField(max_length=16, verbose_name='Sarlavha')),
                ('more_info', models.CharField(max_length=128, verbose_name="Ko'proq ma'lumot")),
            ],
            options={
                'verbose_name': 'Biz haqimizda',
                'verbose_name_plural': 'Biz haqimizda',
            },
        ),
    ]
