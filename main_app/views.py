from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Game
from .models import Show
from .forms import GameForm

# Create your views here.
def index(request):

	games = Game.objects.all()
	form = GameForm()

	return render(request, 'index.html', {'games': games, 'form': form})

def shows(request):

	shows = Show.objects.all()

	return render(request, 'shows.html', {'shows': shows})

def post_game(request):
	form = GameForm(request.POST)
	if form.is_valid():
		game = Game(name = form.cleaned_data['name'],
				    release = form.cleaned_data['release'])
		game.save()
	return HttpResponseRedirect('/')