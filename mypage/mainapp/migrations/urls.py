from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    
    path ('today/',views.today,name='today'),
    path ('random/password/',views.random_password, name='random_password'),
    path('fav/games/', views.FavoriteGames, name= 'favoritegames')

]