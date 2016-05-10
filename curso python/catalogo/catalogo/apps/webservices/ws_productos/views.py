# Create your views here.
from django.http import HttpResponse
from catalogo.apps.ventas.models import *
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("json",Producto.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')


from .serializer import producto_serializer, marca_serializer, categoria_serializer
from rest_framework import viewsets

class producto_viewset(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = producto_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer
		