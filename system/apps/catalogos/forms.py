from django import forms
from apps.catalogos.models import Categoria


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
