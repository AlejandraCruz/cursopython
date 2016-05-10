from rest_framework import serializers
from catalogo.apps.ventas.models import Producto, Marca, Categoria

class producto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('url','descripcion','status', 'nombre', 'imagen', 'precio', 'stock', 'Marca', 'categoria',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url','nombre', )

class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url','nombre', )