from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.catalogos.forms import CategoriaForm
from apps.catalogos.models import Categoria
from apps.generales.views import SinPrivilegios


class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "catalogos/categoria_list.html"
    context_object_name = "obj"
    login_url = 'generales:login'


class CategoriaNew(SuccessMessageMixin, LoginRequiredMixin, SinPrivilegios,
                   generic.CreateView):
    permission_required = "catalogos.add_categoria"
    model = Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")
    success_message = "Categoría Creada Satisfactoriamente"


class CategoriaEdit(LoginRequiredMixin, SinPrivilegios, generic.UpdateView):
    permission_required = "catalogos.change_categoria"
    model = Categoria
    template_name = "catalogos/categoria_form.html"
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy("catalogos:categoria_list")


class CategoriaDel(LoginRequiredMixin, SinPrivilegios, generic.DeleteView):
    permission_required = "catalogos.delete_categoria"
    model = Categoria
    template_name = "catalogos/catalogos_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("catalogos:categoria_list")
