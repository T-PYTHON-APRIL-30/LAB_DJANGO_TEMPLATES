from django.shortcuts import render
from django.http import HttpRequest

from datetime import date
import string

# Create your views here.
def today(request: HttpRequest):
    context = {"date": date.today()}
    return render(request, 'main_app/today.html', context)


def password(request: HttpRequest):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    
    context = {"alphabet": alphabet, "range": range(10)}
    return render(request, 'main_app/password.html', context)


def games(request: HttpRequest):
    fav_game = ["Chess", "Football", "Blot"]

    context = {"fav_game": fav_game}
    return render(request, 'main_app/games.html', context)
