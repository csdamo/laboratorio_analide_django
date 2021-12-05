from django.contrib import admin
from exames.models import Exame, RequisicaoExame, Medico, ResultadoExame


class ListandoExames(admin.ModelAdmin):
    list_display = ('id', 'nome_do_exame')
    list_display_links = ('id', 'nome_do_exame')
    search_fields = ('nome_do_exame',)
    list_per_page = 10

class ListandoResultados(admin.ModelAdmin):
    list_display = ('id','tipo_exame')
    list_display_links = ('id',)
    list_per_page = 10


class ListandoRequisicaoExame(admin.ModelAdmin):
    list_display = ('id', 'nome_paciente', 'nome_do_exame',)
    list_display_links = ('id', 'nome_paciente', 'nome_do_exame')
    search_fields = ('nome_paciente', 'nome_do_exame')
    list_filter = ('nome_paciente', 'nome_do_exame')
    list_per_page = 10

"""class ListandoMedico(admin.ModelAdmin):
    list_display = ('id', 'medico',)
    list_display_links = ('id', 'medico')
    list_per_page = 10"""



admin.site.register(Exame, ListandoExames)
# admin.site.register(RequisicaoExame, ListandoRequisicaoExame)
# admin.site.register(Medico)
admin.site.register(ResultadoExame, ListandoResultados)
