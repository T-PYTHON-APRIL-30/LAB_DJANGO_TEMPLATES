from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import random
import secrets
import string


# Create your views here.

def home_page(request:HttpResponse):
    return render(request, "main_app/home.html")

def today_date(request:HttpResponse):
    context = {"date":date.today()}
    return render(request, "main_app/today.html" ,context)

def random_password(request:HttpResponse):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation
    alphabet = letters + digits + special_char
    pwd_length = 6
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    context = {"pass":pwd}
    return render(request,"main_app/pass.html", context)

def fav_games(request):
    games = ["game1" , "game2"]
    context = {"games" : games}
    return render(request, "main_app/fave_games.html", context)
