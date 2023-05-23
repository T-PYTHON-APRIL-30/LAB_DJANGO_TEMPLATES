from django.shortcuts import render

from django.utils.crypto import get_random_string
import datetime

# Create your views here.

def today(request):
    today_date = datetime.datetime.now().date()
    return render(request, 'app/today.html', {'today_date': today_date})

def random_password(request):
    password = get_random_string(length=10)
    return render(request, 'app/random_password.html', {'password': password})

def favorite_games(request):
    games = ['Game 1', 'Game 2', 'Game 3']
    return render(request, 'app/favorite_games.html', {'games': games})