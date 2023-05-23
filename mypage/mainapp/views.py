from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
import string
from datetime import date 




# Create your views here.
def today(request):
 today_date=date.date.today()
 return render(request, 'today.html',{'today_date':today_date}) 

def random_password(request):
    length = 10
    chars= string.ascii_letters+string.digits+'!@#45678()'
    password="".join(random.choice(chars)for i in range(length))
    return render(request, 'random_password.html',{'password': password})

def favorit_game(request):
   games=['crach', 'hay day', 'onu']
   return render (request, 'games/favorite_games.html', {'games':games})