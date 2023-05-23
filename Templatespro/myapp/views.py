from django.shortcuts import render
from django.utils.crypto import get_random_string
from datetime import date

def today(request):
    today = date.today()
    return render(request, 'myapp/today.html', {'today': today})

def random_password(request):
    password = get_random_string(length=10)
    return render(request, 'myapp/password.html', {'password': password})

def favorite_games(request):
    games = ['Game 1', 'Game 2', 'Game 3']
    return render(request, 'myapp/games.html', {'games': games})
