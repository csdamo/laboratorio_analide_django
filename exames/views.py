from django.shortcuts import render, get_object_or_404, redirect
from .models import Exame, ResultadoExame, RequisicaoExame
from django.contrib.auth.models import User


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


def requisicao(request):
    """if request.method == 'POST':
        nome_do_exame = request.POST['nome_do_exame']
        nome_paciente = request.POST['nome_paciente']
        medico_requerente = get_object_or_404(User, pk=request.user.id)

        requisicao = RequisicaoExame.objects.create(medico_requerente=medico_requerente, nome_paciente=nome_paciente, nome_do_exame=nome_do_exame,)
        requisicao.save()
        return redirect('index')
    else:"""
    return render(request, 'cadastrar_requisicoes.html')
