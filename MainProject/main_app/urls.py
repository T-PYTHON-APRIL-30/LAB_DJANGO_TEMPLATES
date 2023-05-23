from django.urls import path
from . import views

app_name="main_app"

urlpatterns = [
    path("today/",views.today_page,name="today_page"),
    path("random/password/",views.random_page,name="random_page"),
    path("favs/games/",views.fav_page,name="fav_page")
]
