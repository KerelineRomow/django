from django.shortcuts import render

def home(request):
    return render(request, 'cars/index.html',
                  {'title': 'Главная (Авто)', 'brand': 'Все марки'})

def toyota(request):
    return render(request, 'cars/index.html',
                  {'title': 'Тойота', 'brand': 'Toyota'})

def honda(request):
    return render(request, 'cars/index.html',
                  {'title': 'Хонда', 'brand': 'Honda'})

def renault(request):
    return render(request, 'cars/index.html',
                  {'title': 'Рено', 'brand': 'Renault'})
