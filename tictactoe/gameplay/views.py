from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Game

@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, "gameplay/game_detail.html", {'game': game})

# Create your views here.
