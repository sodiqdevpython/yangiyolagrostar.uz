from django.contrib import admin
from .models import HomeBackground, HomeAboutUs, HomeServices, Products, Worker, News, Contact, Comment

@admin.register(HomeBackground)
class HomeBackgroundAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_name', 'button_link']
    search_fields = ['title']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {"slug": ['title']}

@admin.register(Worker)
class HomeBackgroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    search_fields = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'author')
    search_fields = ['name', 'text']
    prepopulated_fields = {'slug': ('title',)}

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

