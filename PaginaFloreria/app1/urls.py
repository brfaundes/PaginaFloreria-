from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos',views.ProductoViewSet)

urlpatterns= [
    path('', views.index),
    path('Index.html', views.index, name="index"),
    path('registro.html', views.registro),
    path('macetero.html', views.macetero),
    path('flores.html', views.flores),
    path('tierra.html', views.tierra),
    path('tienda.html', views.tienda),
    path('tienda2.html', views.tienda2),
    path('tienda3.html', views.tienda3),
    path('login.html', views.login),
    path('registrar.html', views.login),
    path('listadoProductos.html', views.listadoProductos),
    path('nuevoProducto.html',views.nuevoProducto),
    path('registration/registrar.html', views.registroUsuario),
    path('api/productos', include(router.urls))
    

]