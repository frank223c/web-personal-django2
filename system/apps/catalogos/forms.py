from os.path import dirname

# from astroid import objects
from django import forms

from apps.catalogos.models import Categoria, Producto, SubCategoria


class CategoriaForm(forms.ModelForm):
    """Form definition for Categoria."""

    class Meta:
        """Meta definition for Categoriaform."""

        model = Categoria
        fields = ['descripcion', 'activo']
        labels = {'descripcion': "Descripción de la categoria",
                  'activo': "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    """Form definition for Categoria."""

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(activo=True).order_by('descripcion')
    )

    class Meta:
        """Meta definition for Categoriaform."""

        model = SubCategoria
        fields = ['categoria', 'descripcion', 'activo']
        labels = {
            'categoria': "Categoría",
            'descripcion': "Descripción de la sub categoria",
            'activo': "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"


class ProductoForm(forms.ModelForm):
    """Form definition for Categoria."""

    subcategoria = forms.ModelChoiceField(
        queryset=SubCategoria.objects.filter(
            activo=True).order_by('categoria__descripcion', 'descripcion'),
        empty_label="Selecciones Sub Categoria"
    )

    class Meta:
        """Meta definition for Categoriaform."""

        model = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
