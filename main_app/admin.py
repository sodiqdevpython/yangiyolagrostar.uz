from django.contrib import admin
from .models import (
    HomeBackground, HomeAboutUs, HomeServices,HtmlArticle,
    Products, Worker, News, Contact, Comment, NewsImage
)

@admin.register(HtmlArticle)
class HtmlArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated")
    search_fields = ("title",)
    list_filter = ("created",)
    ordering = ("-created",)

    # Slug maydonini avtomatik to‘ldirish
    prepopulated_fields = {"slug": ("title",)}

@admin.register(HomeBackground)
class HomeBackgroundAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_name', 'button_link']
    search_fields = ['title']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ['title']}

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):  # ⚠️ oldingi nom noto‘g‘ri edi (HomeBackgroundAdmin)
    list_display = ['name', 'position']
    search_fields = ['name']

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 3  # 3 ta rasm joyi bo‘sh tursin
    max_num = 10  # maksimal 10 ta rasm
    fields = ['image']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'author')
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [NewsImageInline]  # ⬅️ bu yerga inline qo‘shildi

@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    search_fields = ('name', 'phone_number', 'text')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'news', 'short_text', 'created_at')
    search_fields = ('name', 'text', 'news__title')
    list_filter = ('created_at', 'news')
    ordering = ('-created_at',)

    def short_text(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')
    short_text.short_description = "Izoh matni"

admin.site.register(HomeAboutUs)
admin.site.register(HomeServices)
