from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
# Create your views here.






def today_time (request:HttpRequest):
    context = {"date": date.today}
    return render (request, 'main_app/today.html', context)

def random_password(request: HttpRequest):
    symbols = ['1','2','3''a','b','d''$','#','&']
    q_list = [random.choice(symbols) for i in range(15)]
    context = {"password":q_list}
    return render (request, "main_app/randompassword.html",  context)

def favorite_game(request:HttpRequest):
    game_list = ['crash','plato','uno']
    context = {"game_list":game_list}
    return render (request,'main_app/games.html', context )
