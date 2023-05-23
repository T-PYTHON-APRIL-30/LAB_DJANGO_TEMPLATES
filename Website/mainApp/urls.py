from . import views
from django.urls import path

appName = 'mainApp'

urlpatterns = [
    path('',views.homePage, name='homePage'),
    path('today/',views.todayPage, name ='todayPage'),
    path('random/password/', views.randomPassword, name='randomPassword'),
    path('favs/games/',views.favGames,name='favsGame')

]