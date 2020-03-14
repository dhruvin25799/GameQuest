from django.shortcuts import render
from django.views import generic
from .models import Game
# Create your views here.


class GameList(generic.ListView):
    model = Game
    template_name = 'game_list.html'
