from django.urls import path
from . import views

urlpatterns = [
    path('crear/usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear/libro/', views.crear_libro, name='crear_libro'),
    path('crear/review/', views.crear_review, name='crear_review'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('reviews/', views.lista_reviews, name='lista_reviews'),
]
