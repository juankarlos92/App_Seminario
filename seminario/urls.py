from django.urls import path
from .views import ComentarioListCreateView, MascotaListCreateView, PublicacionListCreateView

urlpatterns = [
    path('api/mascotas/', MascotaListCreateView.as_view(), name='mascota-list-create'),
    path('api/publicaciones/', PublicacionListCreateView.as_view(), name='publicacion-list-create'),
    path('api/comentarios/', ComentarioListCreateView.as_view(), name='comentario-list-create'),
]
