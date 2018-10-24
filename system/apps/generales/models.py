from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ClaseModelo(models.Model):
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = _("Clase Modelo")
        verbose_name_plural = _("Clases Modelo")

    def __str__(self):
        return '{}'.format(self.activo)
