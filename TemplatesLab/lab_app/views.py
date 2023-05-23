from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import random
# Create your views here.

def home_page(request:HttpRequest):

    return render(request,"lab_app/home.html")

def date_page(request:HttpRequest):
    context = {"date" : date.today()}
    return render(request,"lab_app/date.html",context)

def randon_pass(request:HttpRequest):
    passchar="abcde$ABCDEFGHIJKLMNOPQRSTUVWXYZfghijklm$nopqr$stuvwxyz1234567890$"
    password=""
    for i in range(10):
        password+=random.choice(passchar)
    context = { "password":password}

    return render(request,"lab_app/password.html",context)

def favs_games(request:HttpRequest):
    my_games = ["Tennis", "CardGame", "Football" , "Playstaion"]
    context = {"my_games":my_games}
    return render(request,"lab_app/games.html",context)