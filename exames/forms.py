from django import forms
from datetime import datetime

from .models import RequisicaoExame, ResultadoExame

class DateImput(forms.DateInput):
    input_type = 'date'

class RequisicaoForm(forms.ModelForm):
    class Meta:
        model = RequisicaoExame
        fields = '__all__'

        widgets = {
            'date_da_requisicao': DateImput(),
        }


class ResultadoForms(forms.ModelForm):
    date_do_resultado = forms.DateField(label='Data do resultado', initial=datetime.today)
    class Meta:
        model = ResultadoExame

        fields = [
            'requisicao',
            'nome_do_exame',
            'nome_paciente',
            'medico_requerente',
            'date_do_resultado',
            'laudo_exame',

            ]

        widgets = {
            'date_do_resultado': DateImput(),
        }