from django.db import models


class Club(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return f"Club: {self.nombre}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - Categoria: {self.categoria}"
