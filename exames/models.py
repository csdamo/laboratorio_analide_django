from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


TIPO_EXAME = (
        ('glicose', 'glicose'),
        ('colesterol', 'colesterol'),
        ('testecovid', 'teste Covid'),
        ('testetoxicologico', 'teste toxicológico'),
)

TIPO_RESULTADO = (
        ('positivo', 'positivo'),
        ('negativo', 'negativo'),
        ('NSA', 'NSA'),
)


class Exame(models.Model):
    nome_do_exame = models.CharField(max_length=200)
    preparo_para_exame = models.TextField(blank=True, null=True)  # alteração não migrada
    sobre_o_exame = models.TextField(blank=True, null=True)  # alteração não migrada
    tempo_para_realizacao_exame = models.IntegerField(default=0)  # alteração não migrada
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_exame = models.ImageField(upload_to='fotos/%d/%m/%y/', blank=True)
    publicada = models.BooleanField(default=False)
    tipo_exame = models.CharField(
        max_length=100,
        choices=TIPO_EXAME,
        default='glicose')

    def __str__(self):
        return self.nome_do_exame


class Medico(models.Model):
    medico = models.CharField(max_length=100)

    def __str__(self):
        return self.medico


class RequisicaoExame(models.Model):
    nome_do_exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    nome_paciente = models.ForeignKey(User, on_delete=models.CASCADE,)
    medico_requerente = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True)
    date_da_requisicao = models.DateTimeField(default=datetime.now, blank=True)


class ResultadoExame(models.Model):
    requisicao = models.ForeignKey(RequisicaoExame, on_delete=models.CASCADE, blank=True)
    nome_do_exame = models.ForeignKey(Exame, on_delete=models.CASCADE, blank=True)
    nome_paciente = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    medico_requerente = models.ForeignKey(Medico, on_delete=models.CASCADE, blank=True)
    date_do_resultado = models.DateTimeField(default=datetime.now, blank=True)
    laudo_exame = models.TextField(blank=True, null=True)
    arquivo_exame = models.ImageField(upload_to='fotos/%d/%m/%y/', blank=True)
    publicada = models.BooleanField(default=False)

    tipo_exame = models.CharField(
        max_length=100,
        choices=TIPO_EXAME,
        default='glicose')

    indice_glicose = models.CharField(max_length=100, blank=True, null=True)
    indice_colesterol = models.CharField(max_length=100, blank=True, null=True)
    resultado_teste_covid = models.CharField(
        max_length=100,
        choices=TIPO_RESULTADO,
        default='NSA',
        )

    resultado_teste_toxicológico = models.CharField(
        max_length=100,
        choices=TIPO_RESULTADO,
        default='NSA')
