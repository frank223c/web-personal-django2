from django.urls import path

from apps.catalogos.views import (CategoriaDel, CategoriaEdit, CategoriaNew,
                                  CategoriaView, ProductoDel, ProductoEdit,
                                  ProductoNew, ProductoView, SubCategoriaDel,
                                  SubCategoriaEdit, SubCategoriaNew,
                                  SubCategoriaView)

urlpatterns = [
    path('categorias', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/delete/<int:pk>',
         CategoriaDel.as_view(), name='categoria_delete'),
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit7<int:pk>',
         SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/delete/<int:pk>',
         SubCategoriaDel.as_view(), name='subcategoria_delete'),
    path('productos', ProductoView.as_view(), name='producto_list'),
    path('productos/new', ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/delete/<int:pk>',
         ProductoDel.as_view(), name='producto_delete'),
]
