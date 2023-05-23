from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import string
import random
# Create your views here.

def today(request:HttpRequest):
    today = {"date":date.today()}
    return render(request, "main_app/date.html", today)

def random_password(request:HttpRequest):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(8))
    final = {"passwordd":result_str}
    return render(request, "main_app/random_password_generation.html", final)

def favs_games(request:HttpRequest):
    games = ["chess",'squence','solitar']
    fav_games = {"games":games}
    return render(request, "main_app/favorits.html", fav_games)    