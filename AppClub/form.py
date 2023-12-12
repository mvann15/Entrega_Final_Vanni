from django import forms

from AppClub.models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ("usuario", "noticia", "comentario")