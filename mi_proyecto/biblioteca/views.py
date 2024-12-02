from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LibroForm, ReviewForm
from .models import Usuario, Libro

# Vista para crear un usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'biblioteca/crear_usuario.html', {'form': form})

# Vista para crear un libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

# Vista para crear una review
def crear_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reviews')
    else:
        form = ReviewForm()
    return render(request, 'biblioteca/crear_review.html', {'form': form})

# Vista para mostrar la lista de usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'biblioteca/lista_usuarios.html', {'usuarios': usuarios})

# Vista para mostrar la lista de libros
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

# Vista para mostrar la lista de reviews
def lista_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'biblioteca/lista_reviews.html', {'reviews': reviews})
