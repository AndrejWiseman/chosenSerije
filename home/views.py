from django.shortcuts import render
from django.db.models import Count
from itertools import chain
import itertools
from operator import attrgetter

from filmovi.models import Filmovi
from serije.models import Serije


# Create your views here.
def index(request):

    film = Filmovi.objects.all().order_by('-date')
    serija = Serije.objects.all().order_by('-date')

    sortirano = sorted(chain(film, serija), key=attrgetter('date'), reverse=True)
    combined = sortirano[0:6]

    context = {
        'combined': combined,
    }

    return render(request, 'index.html', context)

