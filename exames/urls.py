from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exame<int:exame_id>', views.exame, name='exame'),
    path('resultados_dos_exames', views.resultados_dos_exames, name='resultados_dos_exames'),
    path('resultado/<int:resultado_id>', views.resultado, name='resultado'),
    path('requisicao', views.requisicao_list, name='requisicao_list'),
    path('cadastrar_resultado/<int:requisicao_id>', views.cadastrar_resultado, name='cadastrar_resultado'),
]
