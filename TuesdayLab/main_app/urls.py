from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("today/", views.today_page, name="today_page"),
    path("random/password/", views.password_page, name="password_page"),
    path("favs/games/", views.games_page, name="games_page"),

]