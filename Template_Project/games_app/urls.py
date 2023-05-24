from django.urls import path
from . import views

name = "games_app"

urlpatterns = [
    path("today/",views.date, name = "date"),
    path("random/password/",views.pass_generater, name = "pass_generater"),
    path("favs/games/",views.fav_games,name = "fav_games")
]
