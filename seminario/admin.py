from django.contrib import admin
from .models import Usuario, Mascota, Publicacion, Comentario

# Registra el modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nombre_completo')  # Campos que se mostrarán en la lista
    search_fields = ('username', 'email')  # Permite buscar por estos campos

# Registra el modelo Mascota
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'edad', 'dueño')  # Campos que se mostrarán en la lista
    list_filter = ('tipo',)  # Filtra por tipo de mascota
    search_fields = ('nombre', 'dueño__username')  # Permite buscar por nombre o dueño

# Registra el modelo Publicacion
@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'mascota', 'fecha_creacion')  # Campos que se mostrarán en la lista
    list_filter = ('fecha_creacion',)  # Filtra por fecha de creación
    search_fields = ('titulo', 'descripcion')  # Permite buscar por título o descripción

# Registra el modelo Comentario
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'usuario', 'publicacion', 'fecha_creacion')  # Campos que se mostrarán en la lista
    list_filter = ('fecha_creacion',)  # Filtra por fecha de creación
    search_fiel = ('contenido', 'usuario__username')  # Permite buscar por contenido o usuario