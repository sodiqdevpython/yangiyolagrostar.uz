from django.db import models
from django.contrib.auth.models import User
import html
import bleach
from django.utils.text import slugify
import os
from django.utils import timezone
import base64, mammoth

class HomeBackground(models.Model):
    title = models.CharField(max_length=64, verbose_name='Sarlavha')
    button_name = models.CharField(max_length=32, verbose_name="Tugma nomi")
    button_link = models.URLField(verbose_name="Tugma uchun manzil")
    image = models.ImageField(upload_to='backgrounds', verbose_name="Orqa fon rasmi")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Asosiy orqa fon"
        verbose_name_plural = "Asosiy orqa fonlar"

class HomeAboutUs(models.Model):
    image = models.ImageField(upload_to='about-us', verbose_name='Rasm')
    title = models.CharField(max_length=64, verbose_name='Sarlavha')
    more_info = models.TextField(verbose_name="Ko'proq ma'lumot")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda"


class HomeServices(models.Model):
    classname = models.CharField(max_length=64, verbose_name='Class nomi')
    title = models.CharField(max_length=64, verbose_name='Sarlavha')
    more_info = models.CharField(max_length=256, verbose_name="Ko'proq ma'lumot")
    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"

class Products(models.Model):
    title = models.CharField(max_length=128, verbose_name="Mahsulot", unique=True)
    slug = models.SlugField(unique=True, verbose_name="Slug buni yozmang o'zi yozadi")
    text = models.TextField(verbose_name="Ko'proq ma'lumot")
    image = models.ImageField(upload_to='products', verbose_name='Rasm')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"

class Worker(models.Model):
    name = models.CharField(max_length=64, verbose_name="Xodimning ism, familiyasi")
    position = models.CharField(max_length=64, verbose_name="Xodimning lavozimi")    
    image = models.ImageField(upload_to='employe', verbose_name="Xodimning rasmi")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"

class News(models.Model):
    title = models.CharField(verbose_name="Sarlavha", max_length=256, unique=True)
    slug = models.SlugField(verbose_name="Slug buni yozmang o'zi yozadi", unique=True)
    text = models.TextField(verbose_name="Yangilik haqida to'liq shu yerda yozing")
    image = models.ImageField(verbose_name="Yangilik rasmi", upload_to='image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title[:20])

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    text = models.CharField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Xabar"
        verbose_name_plural = "Qoldirilgan xabarlar"


class Comment(models.Model):
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=64)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.text[:30]}"

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created_at']
    

class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return f"{self.news.title} - image"

def article_upload_to(instance, filename):
    return os.path.join("articles", timezone.now().strftime("%Y/%m/%d"), filename)

class HtmlArticle(models.Model):
    title = models.CharField("Sarlavha", max_length=256, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    html_file = models.FileField("HTML hujjat", upload_to=article_upload_to)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "HTML maqola"
        verbose_name_plural = "HTML maqolalar"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_html_content(self):
        """.html faylni matn sifatida o‘qish"""
        if not self.html_file:
            return ""
        try:
            with open(self.html_file.path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"<p>Xatolik yuz berdi: {e}</p>"