from django.urls import path
from . import views


app_name = 'main_app'

urlpatterns = [
    path('today/', views.today, name = 'today'),
    path('random/password/', views.password, name = 'password'),
    path('favs/games/', views.games, name = 'games')
]
