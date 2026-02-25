from django.shortcuts import render
from django.http import HttpResponse

def get_menu():
    return """
        <nav>
            <a href='/'>Главная</a> | 
            <a href='/news/'>Новости</a> | 
            <a href='/management/'>Руководство</a> | 
            <a href='/facts/'>Факты</a> | 
            <a href='/contacts/'>Контакты</a> | 
            <a href='/history/'>История</a> | 
            <a href='/history/people/'>Люди</a> | 
            <a href='/history/photos/'>Фото</a>
        </nav>
        <hr>
    """

def index(request):
    return HttpResponse(get_menu() + "<h2>Киев — столица Украины</h2><p>Добро пожаловать в главный город страны.</p>")

def news(request):
    return HttpResponse(get_menu() + "<h2>Новости города</h2><p>В Киеве восстановили историческое здание на Подоле.</p>")

def management(request):
    return HttpResponse(get_menu() + "<h2>Руководство города</h2><p>Мэр города: Виталий Кличко.</p>")

def facts(request):
    return HttpResponse(get_menu() + "<h2>Факты о городе</h2><p>Киев — один из старейших городов Европы, основанный более 1500 лет назад.</p>")

def contacts(request):
    return HttpResponse(get_menu() + "<h2>Контактные телефоны</h2><p>Справочная служба: 1551</p>")

def history(request):
    return HttpResponse(get_menu() + "<h2>История Киева</h2><p>Общая информация об основании города легендарными братьями Кием, Щеком, Хоривом и сестрой Лыбедью.</p>")

def history_people(request):
    return HttpResponse(get_menu() + "<h2>Знаменитые жители</h2><p>Киев подарил миру таких личностей, как Борис Патон и Игорь Сикорский.</p>")


def history_photos(request):
    photo_url = "https://relax.com.ua/wp-content/media/kiew/2014/01/kiev-album_004.jpg"

    return HttpResponse(
        get_menu() +
        "<h2>Исторические фотографии</h2>" +
        "<p>На фото: Андреевская церковь — жемчужина барокко, возвышающаяся над историческим Подолом.</p>" +
        f"<img src='{photo_url}' alt='Андреевская церковь' style='width:600px; height:auto;'>"
    )

