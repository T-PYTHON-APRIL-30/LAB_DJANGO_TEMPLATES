from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('today/',views.today_date,name="today_page"),
    path('random/password/', views.random_password, name="about_page"),
    path ('favs/games/', views.fav_games,name="fav_games")
]