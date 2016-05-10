from django.conf.urls.defaults import patterns, url
from django.conf.urls import include

from rest_framework import routers
from catalogo.apps.webservices.ws_productos.views import producto_viewset, marca_viewset, categoria_viewset
router = routers.DefaultRouter()
router.register(r'productos', producto_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)

urlpatterns = patterns('catalogo.apps.webservices.ws_productos.views',
		url(r'^ws/productos/$','ws_productos_view',name = 'ws_productos_url'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
	
	)





		