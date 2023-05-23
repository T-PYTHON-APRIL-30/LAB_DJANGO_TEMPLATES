from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime
import random
import string

# Create your views here.

def date(request :HttpRequest):
   
    context = {"date":datetime.now()}

    return render(request , "games_app/today.html",context)

def pass_generater(request :HttpRequest):
        # choose from all lowercase letter
    length = 8
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    context = {"Random":result_str}

    return render (request , "games_app/password.html",context)

def fav_games(request :HttpRequest):
    context = {"games":["8 Ball Pool","Spider","Call of Duty","Subway Surf"]}
    return render (request,"games_app/games.html",context)