from rest_framework import serializers
from .models import Usuario, Mascota, Publicacion, Comentario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'nombre_completo']


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'
        extra_kwargs = {'dueño': {'required': True}}


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'contenido', 'fecha_creacion', 'usuario', 'publicacion']
        read_only_fields = ['fecha_creacion', 'usuario']  # Estos campos no se envían desde el frontend
