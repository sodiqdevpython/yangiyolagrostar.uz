from modeltranslation.translator import register, TranslationOptions
from .models import HomeBackground, HomeAboutUs, HomeServices, Products, Worker, News

@register(HomeBackground)
class HomeBackgroundTranslation(TranslationOptions):
    fields = ('title', 'button_name')

@register(HomeAboutUs)
class HomeAboutUsTranslation(TranslationOptions):
    fields = ('title', 'more_info')

@register(HomeServices)
class HomeServicesTranslation(TranslationOptions):
    fields = ('title', 'more_info')

@register(Products)
class ProductsTranslation(TranslationOptions):
    fields = ('title', 'text')

@register(Worker)
class WorkerTranslation(TranslationOptions):
    fields = ('position', )

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'text')