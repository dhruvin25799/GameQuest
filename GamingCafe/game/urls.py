from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('',views.GameList.as_view(),name='gamelist'),
]
