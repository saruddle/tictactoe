from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from .forms import InvitationForm
from .models import Invitation
from django.core.exceptions import PermissionDenied


@login_required
def home(request):

    myGames = Game.objects.gamesForUser(request.user)
    activeGames = myGames.active()
    invitations = request.user.invitations_received.all()

    #gamesFirstPlayer = Game.objects.filter(firstPlayer = request.user, status = 'F')
    
    #gamesSecondPlayer = Game.objects.filter(secondPlayer = request.user, status = 'S')

    #allMyGames = list(gamesFirstPlayer) + list(gamesSecondPlayer)

    return render(request, "player/home.html", {'games': activeGames, 'invitations': invitations})

@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})

@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            game = Game.objects.create(firstPlayer=invitation.to_user, secondPlayer = invitation.from_user,)
        invitation.delete()
        return redirect(game)
    else:
        return render(request, "player/accept_invitation_form.html", {'invitation': invitation})
