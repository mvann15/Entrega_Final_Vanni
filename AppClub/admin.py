from AppClub.models import Profesor, Materia
from django.contrib import admin
from django.utils.safestring import mark_safe

admin.site.register(Profesor)
admin.site.register(Materia)


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'mostrar_imagen')
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "Sin imagen"

    mostrar_imagen.short_description = 'Imagen'
