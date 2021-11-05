from django.shortcuts import render, get_object_or_404
from .models import Exame, ResultadoExame

def index(request):
    exames = Exame.objects.all()
    dados = {
        'exames':exames
    }
    return render(request, 'index.html', dados)


def exame(request, exame_id):
    exame = get_object_or_404(Exame, pk=exame_id)
    exame_a_ser_exibido = {
        'exame':exame
    }
    return render(request, 'exame.html', exame_a_ser_exibido)


def resultados_dos_exames(request):
    resultados_dos_exames = ResultadoExame.objects.all()
    dados = {
        'resultados':resultados_dos_exames,
    }
    return (request, 'dashboard.html', dados)


def resultado(request, resultado_id):
    resultado = get_object_or_404(ResultadoExame, pk=resultado_id)
    resultado_a_ser_exibido = {
        'resultado':resultado
    }
    return render(request, 'resultado.html', resultado_a_ser_exibido)
