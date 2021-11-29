import datetime

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import date

from .models import Exame, ResultadoExame, RequisicaoExame, Medico
from .forms import ResultadoForms
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
    # requisicao_dos_exames = RequisicaoExame.object.all()
    dados = {
        'resultados': resultados_dos_exames,
        # 'requisicoes': requisicao_dos_exames,
    }
    return (request, 'dashboard.html', dados)


def resultado(request, resultado_id):
    resultado = get_object_or_404(ResultadoExame, pk=resultado_id)
    # requisitos = get_object_or_404(RequisicaoExame, pk=resultado_id)
    resultado_a_ser_exibido = {
        'resultado':resultado,
        # 'requisitos':requisitos,
    }
    return render(request, 'resultado.html', resultado_a_ser_exibido)


def requisicao_list(request):

    if request.user.is_authenticated:
        id = request.user.id
        if request.user.is_superuser:
            requisicoes = RequisicaoExame.objects.all()
            dados = {
                'requisicoes': requisicoes
            }
            return render(request, 'requisicao_list.html', dados)
        elif request.user.is_staff:
            nome = request.user.username
            nome_str = str(nome)
            med = get_object_or_404(Medico, medico=nome_str)
            id_med = med.id
            requisicoes = RequisicaoExame.objects.all().filter(medico_requerente=id_med)
            dados = {
                'requisicoes': requisicoes
            }
            return render(request, 'requisicao_list.html', dados)


        else:
            requisicoes = RequisicaoExame.objects.all().filter(nome_paciente=id)
            dados = {
                'requisicoes': requisicoes
            }
            return render(request, 'requisicao_list.html', dados)



# MÉTODO PARA USO DO FORMS com laudo prépreenchido
def cadastrar_resultado(request, requisicao_id):
    requisicao = get_object_or_404(RequisicaoExame, pk=requisicao_id)

    if str(requisicao.nome_do_exame) == 'teste de glicose':
        form = ResultadoForms(initial={
            'requisicao': requisicao,
            'nome_do_exame': requisicao.nome_do_exame,
            'nome_paciente': requisicao.nome_paciente,
            'medico_requerente': requisicao.medico_requerente,
            'laudo_exame': 'glicemia em jejum mg/dl: '
        })

    if str(requisicao.nome_do_exame) == 'teste de colesterol':
        form = ResultadoForms(initial={
            'requisicao': requisicao,
            'nome_do_exame': requisicao.nome_do_exame,
            'nome_paciente': requisicao.nome_paciente,
            'medico_requerente': requisicao.medico_requerente,
            'laudo_exame': 'Colesterol LDL em mg/dl: '
        })

    if str(requisicao.nome_do_exame) == 'teste de covid':
        form = ResultadoForms(initial={
            'requisicao': requisicao,
            'nome_do_exame': requisicao.nome_do_exame,
            'nome_paciente': requisicao.nome_paciente,
            'medico_requerente': requisicao.medico_requerente,
            'laudo_exame': 'RT-PCR (P/N): '
        })

    if str(requisicao.nome_do_exame) == 'teste toxicológico':
        form = ResultadoForms(initial={
            'requisicao': requisicao,
            'nome_do_exame': requisicao.nome_do_exame,
            'nome_paciente': requisicao.nome_paciente,
            'medico_requerente': requisicao.medico_requerente,
            'laudo_exame': 'SEGMED - PCP (N/P): '
        })

    contexto = {
        'form': form,
        'requisicao': requisicao
    }

    if request.method == 'POST':
        form = ResultadoForms(request.POST)
        if form.is_valid():
            resultado = form.save(commit=False)
            resultado.save()
            messages.success(request, 'Resultado cadastrado com sucesso')
            return redirect('requisicao_list')

        else:
            messages.warning(request, 'Registro não foi salvo')
            return render(request, 'cadastrar_resultado.html', contexto)
    return render(request, 'cadastrar_resultado.html', contexto)

# FIM METODO USO FORMS  com laudo pré-preenchido



# MÉTODO PARA USO DO FORMS
"""def cadastrar_resultado(request, requisicao_id):
    requisicao = get_object_or_404(RequisicaoExame, pk=requisicao_id)

    form = ResultadoForms(initial={
        'requisicao': requisicao,
        'nome_do_exame': requisicao.nome_do_exame,
        'nome_paciente': requisicao.nome_paciente,
        'medico_requerente': requisicao.medico_requerente,
    })

    contexto = {
        'form': form,
        'requisicao': requisicao
    }

    if request.method == 'POST':
        form = ResultadoForms(request.POST)
        if form.is_valid():
            resultado = form.save(commit=False)
            resultado.save()
            messages.success(request, 'Resultado cadastrado com sucesso')
            return redirect('requisicao_list')

        else:
            messages.warning(request, 'Registro não foi salvo')
            return render(request, 'cadastrar_resultado.html', contexto)
    return render(request, 'cadastrar_resultado.html', contexto)"""

# FIM METODO USO FORMS


# METODO FORMULARIO DIRETO NO HTML
"""def cadastrar_resultado(request, requisicao_id):
    requisicao = get_object_or_404(RequisicaoExame, pk=requisicao_id)

    form = ResultadoForms(initial={
        'requisicao': requisicao,
        'nome_do_exame': requisicao.nome_do_exame,
        'nome_paciente': requisicao.nome_paciente,
        'medico_requerente': requisicao.medico_requerente,
    })

    contexto = {
        'form': form,
        'requisicao': requisicao
    }
    if request.method == 'POST':
        requisicao = requisicao.id
        nome_do_exame = request.POST['nome_do_exame']
        nome_paciente = request.POST['nome_paciente']
        medico_requerente = request.POST['medico_requerente']
        date_do_resultado = request.POST['date_do_resultado']
        laudo_exame = request.POST['laudo_exame']
        tipo_exame = request.POST['tipo_exame']
        indice_glicose = request.POST['indice_glicose']
        indice_colesterol = request.POST['indice_colesterol']
        resultado_teste_covid = request.POST['resultado_teste_covid']
        resultado_teste_toxicológico = request.POST['resultado_teste_toxicológico']
        resultado = ResultadoExame.objects.create(
        requisicao=requisicao,
        nome_do_exame =nome_do_exame,
        nome_paciente =nome_paciente,
        medico_requerente=medico_requerente,
        date_do_resultado=date_do_resultado,
        laudo_exame =laudo_exame,
        tipo_exame=tipo_exame,
        indice_glicose=indice_glicose,
        indice_colesterol=indice_colesterol,
        resultado_teste_covid=resultado_teste_covid,
        resultado_teste_toxicológico=resultado_teste_toxicológico
        )

        resultado.save()
        return redirect(requisicao_list)
    else:
        return render(request, 'cadastrar_resultado.html', contexto)"""
# FIM DO MÉTODO FORMULARIO DIRETO NO HTML