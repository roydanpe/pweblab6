from django import forms
from .models import Usuario, Libro, Review

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['libro', 'usuario', 'calificacion', 'comentario']
