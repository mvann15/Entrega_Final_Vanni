from django.shortcuts import render, redirect
from django.views.generic import ListView

from AppClub.form import ComentarioForm
from AppClub.models import Profesor, Materia, Noticia, Comentario


def show_html(request):
    contexto = {"nombre": "UNIVERSITARIO"}
    return render(request, "index.html", contexto)


class ProfesorList(ListView):
    model = Profesor
    template_name = "AppClub/profesor.html"
    context_object_name = 'profesores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context


class MateriaList(ListView):
    model = Materia
    template_name = "AppClub/materia.html"
    context_object_name = 'materias'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = Materia.objects.all()
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
    # formulario = ComentarioForm(request.POST)
    #
    # if formulario.is_valid():
    #     informacion = formulario.cleaned_data

    noticia = Noticia.objects.get(id=request.POST["noticia"])
    comentario_crear = Comentario(usuario=request.user, noticia=noticia, comentario=request.POST["comentario"])

    comentario_crear.save()

    return redirect("/app/noticias")
    #
    # form = ComentarioForm()
    # contexto = {
    #     "form": form
    # }
    # return render(request, "comentario.html", contexto)
