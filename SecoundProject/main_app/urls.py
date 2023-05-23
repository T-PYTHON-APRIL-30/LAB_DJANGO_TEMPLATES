from django.urls import path
from . import views


app_name = 'main_app'


urlpatterns = [
    path("today/", views.today_time, name="today_time"),
    path("random/password/", views.random_password, name="random_password"),
    path("favs/games/", views.favorite_game, name="favorite_game")
    
]