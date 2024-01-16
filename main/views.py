from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request) -> HttpResponse:

    context = {
        'title': 'WW - главная',
        'content': 'Магазин мебели WoodWonders',
    }

    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context = {
        'title': 'WW - О нас',
        'content': 'О нас',
        'text_on_page': 'Почему этот магазин хороший'
    }

    return render(request, 'main/about.html', context)
