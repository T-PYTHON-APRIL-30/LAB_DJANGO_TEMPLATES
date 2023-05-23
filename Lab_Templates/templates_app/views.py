from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import string
import random

# Create your views here.

today_date_dic = {"today_date_k": date.today()}

def today_date(request:HttpRequest):

    return render (request, "templates_app/date.html", today_date_dic)


def random_pass(request:HttpRequest):
    password = ""
    length = 8
    random_pass = string.ascii_letters + string.digits + string.punctuation
    
    for i in range(length):
        password += random.choice(random_pass)
        
    pass_dict = {"random_pass":password}

    return render(request, "templates_app/random_pass.html", pass_dict)


def fav_games(request:HttpRequest):

    my_fav_games = {"game1":"Battlefield","game2": "FIFA","game3": "Apex_Legends"}


    return render(request, "templates_app/fav_games.html", my_fav_games)