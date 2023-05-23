from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
import random


# Create your views here.
def homePage(request:HttpRequest):
    return HttpResponse('Home Page')

def todayPage(request:HttpRequest):
    context = {'today': date.today()}
    return render(request,'mainApp/today.html',context)

def randomPassword(request:HttpRequest):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_-'
    password = [random.choice(characters) for i in range (12)]
                
    context = {'Password':password}
    return render(request,'mainApp/password.html',context)

def favGames(request:HttpRequest):
    context = {'games': ['Carsh','Spyro','Tekken','Super Mario']}
    return render(request,'mainApp/games.html',context)