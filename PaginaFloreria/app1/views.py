from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .models import Producto
from .forms import ProductoForm, CustomUserForm
from  django.contrib.auth import login, authenticate

#rest_framework

from rest_framework import viewsets
from .serializers import ProductoSerializer

# Create your views here.

TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def index(request):
    return render(request, "core/index.html")

def registro(request):
    return render(request, "core/registro.html")

def macetero(request):

    return render(request, "core/macetero.html")

def flores(request):
    return render(request, "core/flores.html")

def tierra(request):
    return render(request, "core/tierra.html")

def tienda(request):
    return render(request, "core/tienda.html")

def tienda2(request):
    return render(request, "core/tienda2.html")

def tienda3(request):
    return render(request, "core/tienda3.html") 

def login(request):
    return render(request, "registration/login.html") 

def registroUsuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            data['mensaje'] = "registrado correctamente..."
            return redirect(to='login')


    return render(request, 'registration/registrar.html', data)

def listadoProductos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listadoProductos.html', data)

def nuevoProducto(request):
    data = {
    'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Agregado Correctamente..."

    return render(request, 'core/nuevoProducto.html',data)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    