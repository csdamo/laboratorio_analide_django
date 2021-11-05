from django.contrib import admin
from exames.models import Exame, ResultadoExame


class ListandoExames(admin.ModelAdmin):
    list_display = ('id', 'nome_do_exame', 'valor_exame')
    list_display_links = ('id', 'nome_do_exame')
    search_fields = ('nome_do_exame',)
    list_per_page = 10

class ListandoResultados(admin.ModelAdmin):
    list_display = ('id', 'nome_paciente','nome_do_exame', 'publicada')
    list_display_links = ('id', 'nome_paciente','nome_do_exame')
    search_fields = ('nome_paciente', 'nome_do_exame')
    list_filter = ('nome_paciente', 'nome_do_exame')
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Exame, ListandoExames)
admin.site.register(ResultadoExame, ListandoResultados)
