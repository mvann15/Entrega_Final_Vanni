from django.shortcuts import render, redirect
from django.views.generic import ListView

from AppClub.models import Profesor, Materia, Noticia, Comentario, Perfil


def show_html(request):
    contexto = {"nombre": "UNIVERSITARIO"}
    return render(request, "index.html", contexto)


class ProfesorList(ListView):
    model = Profesor
    template_name = "AppClub/profesor.html"
    context_object_name = 'profesores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesores = Profesor.objects.all()
        context['profesores'] = profesores
        context['base_de_datos_vacia'] = not profesores.exists()
        return context


class MateriaList(ListView):
    model = Materia
    template_name = "AppClub/materia.html"
    context_object_name = 'materias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        materias = Materia.objects.all()
        context['materias'] = materias
        context['base_de_datos_vacia'] = not materias.exists()
        return context


class NoticiaList(ListView):
    model = Materia
    template_name = "AppClub/noticia.html"
    context_object_name = 'noticias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.all()
        return context


def comentario(request):
    noticia = Noticia.objects.get(id=request.POST["noticia"])
    comentario_crear = Comentario(usuario=request.user, noticia=noticia, comentario=request.POST["comentario"])

    comentario_crear.save()

    return redirect("/app/noticias")


def mi_perfil(request):
    perfil = Perfil.objects.first()
    contexto = {
        'perfil': perfil
    }
    return render(request, 'AppClub/perfil.html', contexto)



