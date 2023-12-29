from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
# en este caso, el campo username es requerido, pero no se usa para el login, solo para identificar al usuario en el admin.
# ademas de que en el admin de django se reemplaza el username por el email del usuario