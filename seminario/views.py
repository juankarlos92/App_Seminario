from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Mascota, Publicacion, Comentario
from .serializers import MascotaSerializer, PublicacionSerializer, ComentarioSerializer
from django.db.utils import IntegrityError

User = get_user_model()

class MascotaListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MascotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicacionListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        publicaciones = Publicacion.objects.all()
        serializer = PublicacionSerializer(publicaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComentarioListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        comentarios = Comentario.objects.all()
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        print("📌 Django recibió:", data)  # Depuración

        try:
            # 🔹 Verificar si "publicacion" está presente
            if "publicacion" not in data:
                return Response({"error": "El campo 'publicacion' es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

            data["publicacion"] = int(data["publicacion"])
            if not Publicacion.objects.filter(id=data["publicacion"]).exists():
                return Response({"error": "La publicación no existe."}, status=status.HTTP_400_BAD_REQUEST)

            # 🔹 Verificar si "usuario" está presente y no es NULL
            if "usuario" not in data or data["usuario"] is None:
                return Response({"error": "El campo 'usuario' es obligatorio y no puede ser NULL."}, status=status.HTTP_400_BAD_REQUEST)

            data["usuario"] = int(data["usuario"])
            if not User.objects.filter(id=data["usuario"]).exists():
                return Response({"error": "El usuario no existe."}, status=status.HTTP_400_BAD_REQUEST)

            # 🔹 Asignar el usuario correctamente
            usuario = User.objects.get(id=data["usuario"])
            publicacion = Publicacion.objects.get(id=data["publicacion"])

            print("📌 Django procesando datos corregidos:", data)  # Depuración final

            # Guardar el comentario asegurando que usuario y publicación no sean NULL
            comentario = Comentario(
                contenido=data["contenido"],
                usuario=usuario,  # Asignar objeto usuario
                publicacion=publicacion  # Asignar objeto publicación
            )
            comentario.save()

            return Response({"mensaje": "Comentario creado con éxito"}, status=status.HTTP_201_CREATED)

        except IntegrityError as e:
            print("❌ Error de integridad en la base de datos:", str(e))  # Mostrar el error en la consola
            return Response({"error": "Error de integridad en la base de datos.", "detalle": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            print("❌ Error inesperado:", str(e))  # Mostrar el error en la consola
            return Response({"error": "Error inesperado.", "detalle": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)