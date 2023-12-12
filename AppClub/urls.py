from django.contrib import admin
from django.urls import path

from AppClub.views import show_html, ProfesorList, MateriaList, NoticiaList, comentario

urlpatterns = [
    path('mostrar/', show_html),
    path('profesores/', ProfesorList.as_view(), name='Profesores'),
    path('materias/', MateriaList.as_view(), name='Materia'),
    path('noticias/', NoticiaList.as_view(), name='Noticia'),
    path('comentarios/', comentario, name="Comentario"),

]
