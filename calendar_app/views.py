from django.shortcuts import render
from datetime import datetime


def show_day(request):
    day_number = datetime.now().weekday()

    days = [
        'Понедельник', 'Вторник', 'Среда',
        'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
    ]

    bg_classes = [
        'monday-bg', 'tuesday-bg', 'wednesday-bg',
        'thursday-bg', 'friday-bg', 'saturday-bg', 'sunday-bg'
    ]

    context = {
        'day_name': days[day_number],
        'bg_style': bg_classes[day_number],
        'current_date': datetime.now().strftime('%d.%m.%Y')
    }

    return render(request, 'calendar_app/index.html', context)
