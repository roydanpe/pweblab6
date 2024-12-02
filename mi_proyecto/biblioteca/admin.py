from django.contrib import admin

# Register your models here.
from .models import Usuario, Libro, Review

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Review)