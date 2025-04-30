from django.shortcuts import render, redirect, get_object_or_404
from .models import HomeBackground, HomeAboutUs, HomeServices, Products, Worker, News
from .forms import ContactForm, CommentForm
from django.core.paginator import Paginator


def home(request):
    home_background = HomeBackground.objects.all()
    home_about_us = HomeAboutUs.objects.all()
    services = HomeServices.objects.all()
    products = Products.objects.all()[:10]
    workers = Worker.objects.all()[:10]
    news = News.objects.order_by('-id')[:3]

    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'home_background': home_background,
        'home_about_us': home_about_us,
        'services': services,
        'products': products,
        'workers': workers,
        'news': news,
        'form': form,
    }

    return render(request, 'index.html', context)

def news_list(request):
    all_news = News.objects.order_by('-id')
    paginator = Paginator(all_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'news_list.html', {'page_obj': page_obj})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    comments = news.comments.all()

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.save()
            return redirect('news_detail', slug=slug)

    context = {
        'news': news,
        'form': form,
        'comments': comments,
    }
    return render(request, 'news_detail.html', context)