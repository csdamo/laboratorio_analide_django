from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exame<int:exame_id>', views.exame, name='exame'),
    path('resultados_dos_exames', views.resultados_dos_exames, name='resultados_dos_exames'),
    path('resultado<int:resultado_id>', views.resultado, name='resultado'),
    path('requisicao', views.requisicao, name='requisicao'),
]
