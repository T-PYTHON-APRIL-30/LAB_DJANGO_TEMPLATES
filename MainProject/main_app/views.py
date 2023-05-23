from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
from datetime import date
import random
def today_page(request:HttpRequest):

    context={"date":date.today()}
    return render(request,"main_app/today.html",context)

def random_page(request:HttpRequest):
    random_choice="qwertyuiplkjhgfdsamnbvcxz0987654321!@#$%^&"
    password=""

    for p in range(8):
        
        password+=random.choice(random_choice)



    context={"password":password}
    return render(request,"main_app/random.html",context)

def fav_page(request:HttpRequest):
    fav=["football","backetball","videogame","swim"]
    context={"favports":fav}
    return render(request,"main_app/favs.html",context)
