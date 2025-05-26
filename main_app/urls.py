from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path("articles/", views.html_article_list, name="article_list"),
    path("articles/<slug:slug>/", views.html_article_detail, name="article_detail"),
]