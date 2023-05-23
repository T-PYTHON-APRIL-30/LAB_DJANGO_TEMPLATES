from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random 
import string
import secrets

# Create your views here.




def today_date(request:HttpRequest):

    context = {"date" : date.today()}
    return render(request, "main_app/today.html", context)

def random_password(request:HttpRequest):
    letters_upper= string.ascii_uppercase
    letters_lower=string.ascii_lowercase
    numbers=string.digits
    all=letters_lower + letters_upper+ numbers
    pw_len=8
    pw = ''
    
    for i in range(pw_len):
        pw += ''.join(secrets.choice(all))
    context = {"random_password":pw}

    return render(request, "main_app/randompassword.html", context)
    # passwords=[random.choices(pw)for i in range(4)]


def fav_games(request:HttpRequest):

    games = ["Crash", "Call of Duty", "Fortnite"]
    context = {"games" : games}
    return render(request, "main_app/favgames.html", context)