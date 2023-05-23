from django.urls import path
from . import views

app_name="main_app"

urlpatterns=[
    path("",views.home_page,name="home_page"),
    path("today/",views.today_tod, name="today"),
    path("random/password/",views.random_password,name="random_password"),
    path("favs/games/",views.favorite_game,name="favGame")
]