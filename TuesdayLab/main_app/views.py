from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import secrets

# Create your views here.
def home_page(request: HttpRequest):


    return render(request, "main_app/home.html")


def today_page(request:HttpRequest):


    context = {"variable" : "today is: ", "date" : date.today()}

    return render(request, "main_app/today.html", context)

def password_page(request:HttpRequest):
    password=secrets.token_urlsafe(10)
    context={"random_password":password}
    return render(request,"main_app/password.html",context)

def games_page(request:HttpRequest):
    favorite_games=["Metal Gear","Devil May Cry","Elden Ring"]
    context= {"list_of_games":favorite_games}
    return render(request,"main_app/games.html",context)
