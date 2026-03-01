from django.shortcuts import render

def home(request):
    return render(request, 'sportblog/index.html',
                  {'title': 'Главная'})

def football(request):
    return render(request, 'sportblog/index.html',
                  {'title': 'Футбол'})

def hockey(request):
    return render(request, 'sportblog/index.html',
                  {'title': 'Хоккей'})

def basketball(request):
    return render(request, 'sportblog/index.html',
                  {'title': 'Баскетбол'})
