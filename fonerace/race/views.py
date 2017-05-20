from django.shortcuts import render

from .race import Race
from .lap import Lap

def index(request):

    race = Race('../race.log')

    classificacao = race.classificacao()
    melhor_volta = race.melhor_volta()
    tempo_total = race.tempo_total_prova()

    return render(request, 'index.html', {'classificacao':classificacao,'melhor_volta':melhor_volta,'tempo_total':tempo_total})
