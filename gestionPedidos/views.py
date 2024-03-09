from django.shortcuts import render
from django.http import HttpResponse
from Tienda_Online import settings
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from gestionPedidos.forms import FormularioContacto



# Create your views here.
def busqueda(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"] != "":
        #mensaje = "El mensaje de la busqueda: %s ha sido encontrado como petición" %request.GET["prd"]
        producto = request.GET["prd"]
        if len(producto)> 20:
            return HttpResponse("Los caracteres del productos son muy largos")
        else:
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "busqueda_articulo.html", {"articulos": articulos, "query": producto})
    else:
        mensaje = "No existe ningun elemento en el input"

    return HttpResponse(mensaje)


def comentario(request):

    if request.method == 'POST':

       miFormulario = FormularioContacto(request.POST)

       if miFormulario.is_valid():
           inf_Forrm = miFormulario.cleaned_data

           send_mail(inf_Forrm["nombre"], inf_Forrm["comentario"],
                      inf_Forrm.get("email", ""), ['sebastianome209@gmail.com'],)

           return render(request, "mensaje.html")
    else: 
        miFormulario = FormularioContacto()

    return render(request, "formulario_contacto.html", {"form": miFormulario})



def holaMundo(request):
    return render(request, "index.html")