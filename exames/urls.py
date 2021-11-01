from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:exame_id>', views.exame, name='exame')
]
