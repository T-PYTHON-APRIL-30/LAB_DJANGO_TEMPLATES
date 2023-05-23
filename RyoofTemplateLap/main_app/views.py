from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random 
# Create your views here.




def today_date(request:HttpRequest):

    context = {"date" : date.today()}
    return render(request, "main_app/today.html", context)

def random_password(request:HttpRequest):
    passwords=['gfgf56_ggg','uuyuyu',"YRD97662kjhh&c","dggR344_dd"]
    context = {"random_password":random.choice(passwords)}

    return render(request, "main_app/randompassword.html", context)



def fav_games(request:HttpRequest):

    games = ["Crash", "Call of Duty", "Fortnite"]
    context = {"favorate_games" : games}
    return render(request, "main_app/favgames.html", context)