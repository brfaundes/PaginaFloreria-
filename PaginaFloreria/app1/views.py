from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse 
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
    return render(request, "registration/login") 