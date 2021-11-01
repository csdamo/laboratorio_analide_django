from django.shortcuts import render, get_object_or_404
from .models import Exame



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

