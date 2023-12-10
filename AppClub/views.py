from django.shortcuts import render
from django.views.generic import ListView
from AppClub.models import Profesor


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
