from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Modelo para los Usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

# Modelo para los Libros
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

# Modelo para las Reviews
class Review(models.Model):
    libro = models.ForeignKey(Libro, related_name='reviews', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='reviews', on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField()  # Calificación entre 1-5
    comentario = models.TextField()

    def __str__(self):
        return f"Review de {self.usuario.nombre} para {self.libro.titulo}"
