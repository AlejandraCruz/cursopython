from django.contrib import admin
from catalogo.apps.ventas.models import Marca, Producto, Categoria


admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Categoria)