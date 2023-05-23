from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page , name="home/"),
    path("today/", views.today_date, name="today/"),
    path("random/password/", views.random_password, name="random/password/"),
    path("fave/games/", views.fav_games, name="fave/games")

]