from django.urls import path
from . import views

app_name = "templates_app"



urlpatterns = [
    path("today/",views.today_date, name="date page"),
    path("random/password/", views.random_pass, name= "random password page"),
    path("favs/games/", views.fav_games, name= "favorite games page")
]