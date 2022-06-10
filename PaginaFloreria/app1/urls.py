from django.urls import path
from . import views

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
    path('login', views.login),

    

]