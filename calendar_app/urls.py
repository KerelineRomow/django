from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_day, name='day_index'),
]
