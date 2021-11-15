from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('exames.urls')),
    path('usuarios/', include('usuarios.urls')),
    # path('requisicao/', include('requisicao.urls')),
    # path('resultado_exame/', include('resultado_exame.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
