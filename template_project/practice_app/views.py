from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
from django.contrib.auth.models import User
# Create your views here.

def homePage(request: HttpRequest):
    return render(request, "practice_app/homePage.html")
def todayPage(request: HttpRequest):
    return render(request,"practice_app/todayPage.html",{"date": date.today()})
def randomPasswordPage(request: HttpRequest):
    return render(request,"practice_app/randomPasswordPage.html", {"password": User.objects.make_random_password(allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789")})
def favGamesPage(request: HttpRequest):
    games = ["Minecraft", "Table tennis", "football"]
    return render(request,"practice_app/favGamesPage.html",{"games": games})