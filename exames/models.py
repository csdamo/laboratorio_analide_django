from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Exame(models.Model):
    nome_do_exame = models.CharField(max_length=200)
    preparo_para_exame = models.TextField()
    sobre_o_exame = models.TextField()
    tempo_para_realizacao_exame = models.IntegerField()
    valor_exame = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_exame = models.ImageField(upload_to='fotos/%d/%m/%y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_do_exame

class ResultadoExame(models.Model):
    nome_do_exame = models.ForeignKey(Exame, on_delete=models.CASCADE)
    nome_paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    medico_requerente = models.CharField(max_length=100)
    date_do_resultado = models.DateTimeField(default=datetime.now, blank=True)
    laudo_exame = models.TextField()
    arquivo_exame = models.ImageField(upload_to='fotos/%d/%m/%y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __int__(self):
        return self.nome_paciente
