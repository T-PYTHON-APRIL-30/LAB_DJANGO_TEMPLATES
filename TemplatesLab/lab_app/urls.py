from django.urls import path
from . import views

app_name = "lab_app"

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path("today/",views.date_page,name="date_page"),
    path("random/password/", views.randon_pass, name="randon_pass"),
    path("favs/games/", views.favs_games,name="favs_games")
]