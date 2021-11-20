from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Usuario(models.Model):
    idUsuario = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ["email"]

    def __str__(self):
        return self.email