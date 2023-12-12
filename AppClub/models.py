from django.db import models
import datetime


class Club(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f"Club: {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    materia = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='profesor_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - Materia: {self.materia}"


class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='materia_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to="noticia_images/", null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f" {self.titulo} "
