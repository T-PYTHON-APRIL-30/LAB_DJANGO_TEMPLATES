from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from datetime import date
import secrets
import string

def home_page(request:HttpRequest):

    return render(request,"main_app/home_page.html")

def today_tod(request:HttpRequest):

    return render(request,"main_app/today.html",{"date":date.today()})

def generate_password(length):
    # Define the pool of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a password of the given length
    password = ''.join(secrets.choice(chars) for i in range(length))

    return password

def random_password(request:HttpRequest):
    return render(request,"main_app/random.html",{"random_password":generate_password(12)})

def favorite_game(request:HttpRequest):
    return render(request,"main_app/game.html",{"gameList":["call of duty","overwatch","fotenight"]})