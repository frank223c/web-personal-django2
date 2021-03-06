from apps.generales.models import ClaseModelo
from django.db import models

from tkinter.constants import CASCADE


# Create your models here.


class Categoria(ClaseModelo):

    descripcion = models.CharField(
        max_length=100, help_text='Descripción de la categoria', unique=True)

    # objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100, help_text='Descripción de la Sub Categoria')

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        # db_table = ''
        # managed = True
        verbose_name = 'Sub Categoria'
        verbose_name_plural = 'Sub Categorias'
        unique_together = ('categoria', 'descripcion')


class Producto(ClaseModelo):

    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100, help_text='Descripción del Producto', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Producto, self).save()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
