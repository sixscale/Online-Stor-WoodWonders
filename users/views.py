from django.shortcuts import render


def login(request):
    context = {
        'title': 'WW - Авторизация',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'WW - Регистрация',
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'WW - Кабинет',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    pass
