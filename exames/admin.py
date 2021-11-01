from django.contrib import admin
from exames.models import Exame


class ListandoExames(admin.ModelAdmin):
    list_display = ('id', 'nome_do_exame', 'valor_exame')
    list_display_links = ('id', 'nome_do_exame')
    search_fields = ('nome_do_exame',)
    list_per_page = 10


admin.site.register(Exame, ListandoExames)
