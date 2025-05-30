# Generated by Django 4.2 on 2025-05-26 03:56

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_newsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True, verbose_name='Sarlavha')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('doc_file', models.FileField(upload_to=main_app.models.article_upload_to, verbose_name='Word hujjat (.docx)')),
                ('html_content', models.TextField(blank=True, editable=False, verbose_name='HTML')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Maqola (Word)',
                'verbose_name_plural': 'Maqolalar (Word)',
                'ordering': ['-created'],
            },
        ),
    ]
