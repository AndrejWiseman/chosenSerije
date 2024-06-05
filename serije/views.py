from django.shortcuts import render, get_object_or_404
from .models import Serije, Epizoda


# Create your views here.
def serije(request):

    serije = Serije.objects.all().order_by('-date')

    context = {
        'serije': serije,
    }

    return render(request, 'serije.html', context)


def serije_detaljno(request, slug):

    s_detaljno = get_object_or_404(Serije, slug=slug)
    epiz = Epizoda.objects.filter(epizode=s_detaljno).order_by('-epizode_date')

    context = {
        's_detaljno': s_detaljno,
        'epizoda': epiz
    }
    return render(request, 'serije-detail.html', context)

