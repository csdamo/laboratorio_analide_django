"""from django.contrib import admin
from django.contrib.auth.models import User

class ListandoUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome_usuario', 'medico')
    list_display_links = ('id', 'nome_usuario',)
    list_editable = ('is_staff',)

admin.site.register(User, ListandoUsuario)

"""
