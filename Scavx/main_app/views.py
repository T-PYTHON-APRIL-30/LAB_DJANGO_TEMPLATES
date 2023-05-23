from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
import random
# Create your views here.

def today_page(request:HttpRequest):
    context={"datetoday": date.today()}
    return render(request,"main_app/today.html",context)

def password_page(request:HttpRequest):
    papers=['a','b','c','d','1','2','3','4','@','-','/','5','n','B']
    paas_list = [random.choice(papers) for i in range(8)]
    context= {"password":"".join(paas_list).replace(" ", "")}
    return render(request,"main_app/password.html",context)

def games_page(request:HttpRequest):
    fav_game=["Call Of Duty","Overwatch","FIFA 23","The Last Of Us"]
    context={"fav_game":fav_game}
    return render(request,"main_app/games.html",context)
