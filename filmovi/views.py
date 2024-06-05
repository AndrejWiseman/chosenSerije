from django.shortcuts import render, get_object_or_404
from .models import Filmovi


# Create your views here.
def filmovi(request):

    filmovi = Filmovi.objects.all().order_by('-date')

    context = {
        'filmovi': filmovi,
    }

    return render(request, 'filmovi.html', context)


def filmovi_detaljno(request, slug):

    f_detaljno = get_object_or_404(Filmovi, slug=slug)

    context = {
        'f_detaljno': f_detaljno,
    }
    return render(request, 'filmovi-detail.html', context)