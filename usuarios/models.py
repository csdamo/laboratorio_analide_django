"""from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    medico = models.BooleanField(default=False)"""



"""from django.db import models
from django.contrib.auth.models import User

class Tipousuario(models.Model):
    nome_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    medico = models.BooleanField(default=False)

    def __str__(self):
        self.nome_usuario"""


"""from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   medico = models.BooleanField(default=False)"""