from django.contrib import admin
from gestionPedidos.models import Articulos, Cliente, Pedidos

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombreCliente", "direccion", "telefono"]
    search_fields = ["nombreCliente", "telefono"]

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ["seccion",]

class PedidosAdmin(admin.ModelAdmin):
    list_display = ["numero", "fecha"]
    list_filter = ["fecha"]
    date_hierarchy = "fecha"

admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedidos, PedidosAdmin)