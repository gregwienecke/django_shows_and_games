from django.shortcuts import render
from django.http import HttpResponse

from .models import Game
from .models import Show

# Create your views here.
def index(request):

	games = Game.objects.all()

	return render(request, 'index.html', {'games': games})

def shows(request):

	shows = Show.objects.all()

	return render(request, 'shows.html', {'shows': shows})