from django.urls import path
from . import views

name = "games_app"

urlpatterns = [
    path("today/",views.date, name = "games_app"),
    path("random/password/",views.pass_generater, name = "games_app"),
    path("favs/games/",views.fav_games,name = "games_app")
]
