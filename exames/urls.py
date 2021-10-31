from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('exame', views.exame, name='exame')
]
