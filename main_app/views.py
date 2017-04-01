from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Game
from .models import Show
from .forms import GameForm, ShowForm

# GAMES
def index(request):

	games = Game.objects.all()
	form = GameForm()

	return render(request, 'index.html', {'games': games, 'form': form})

def post_game(request):
	form = GameForm(request.POST)
	if form.is_valid():
		game = Game(name = form.cleaned_data['name'],
				    release = form.cleaned_data['release'])
		game.save()
	return HttpResponseRedirect('/')


# SHOWS
def shows(request):

	shows = Show.objects.all()
	form = ShowForm()

	return render(request, 'shows.html', {'shows': shows, 'form': form})

def post_show(request):
	form = ShowForm(request.POST)
	if form.is_valid():
		show = Show(name = form.cleaned_data['name'],
				    seen = form.cleaned_data['seen'])
		show.save()
	return HttpResponseRedirect('/shows')