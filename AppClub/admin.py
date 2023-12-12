from AppClub.models import Profesor, Materia, Noticia, Comentario
from django.contrib import admin
from django.utils.safestring import mark_safe

admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Noticia)
admin.site.register(Comentario)


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'materia', 'mostrar_imagen')
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "Sin imagen"

    mostrar_imagen.short_description = 'Imagen'


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'mostrar_imagen')
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "Sin imagen"

    mostrar_imagen.short_description = 'Imagen'


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'mostrar_imagen', "fecha_creacion")
    readonly_fields = ('mostrar_imagen',)

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="50" height="50" />')
        return "Sin imagen"

    mostrar_imagen.short_description = 'Imagen'
