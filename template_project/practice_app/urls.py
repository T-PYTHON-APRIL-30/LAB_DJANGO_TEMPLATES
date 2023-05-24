from django.urls import path
from . import views

app_name = "practice app"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("today/", views.todayPage, name="todayPage"),
    path("random/password", views.randomPasswordPage, name="randomPasswordPage"),
    path("favs/games/", views.favGamesPage, name="favGamesPage")
]