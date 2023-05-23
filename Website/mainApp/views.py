from django.shortcuts import render
from django.http import HttpRequest
from datetime import date
import random


# Create your views here.

def todayPage(request:HttpRequest):
    context = {'today': date.today()}
    return render(request,'mainApp/today.html',context)

def randomPassword(request:HttpRequest):
    passwords = ['akjdjdj33-','jdjjsj553','jhdhdsh77','hhdhdh33','jjdjs66262']
    context = {'Password':random.choice(passwords)}
    return render(request,'mainApp/password.html',context)

def favGames(request:HttpRequest):
    context = {'games': ['Carsh','Spyro','Tekken','Super Mario']}
    return render(request,'mainApp/games.html',context)