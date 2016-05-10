from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'catalogo.views.home', name='home'),
    # url(r'^catalogo/', include('catalogo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^',include('catalogo.apps.home.urls')),
    url(r'^',include('catalogo.apps.ventas.urls')),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^',include('catalogo.apps.webservices.ws_productos.urls')),
    #url(r'^producto/(?P<id_prod>.*)/$', 'single_product_view', name = 'vista_single_producto'),	
)