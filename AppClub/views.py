from django.shortcuts import render
from django.views.generic import ListView
from AppClub.models import Profesor, Materia, Noticia


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
