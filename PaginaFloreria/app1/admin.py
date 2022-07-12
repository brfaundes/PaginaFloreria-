from django.contrib import admin
from .models import Categoria, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock']

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
