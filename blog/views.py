from django.shortcuts import render
from django.utils import timezone
from .models import Registrado, Mascota, Contacto
from .forms import RegForm, ContactForm

# Create your views here.
def base_list(request):
    return render(request, 'blog/base.html')



def registrar_list(request):
    form = RegForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        form_data = form.cleaned_data
        name = form_data.get("nombre_")
        email = form_data.get("email")
        rut = form_data.get("rut")
        fechaNacimiento = form_data.get("fechaNacimiento")
        telefono = form_data.get("telefono")
        calle = form_data.get("calle")
        numero = form_data.get("numero_calle")
        obj = Registrado.objects.create(nombre=name,
        email=email, 
        rut=rut, 
        fechaNacimiento=fechaNacimiento, 
        telefono=telefono, 
        calle=calle, 
        numero_calle=numero)
        
    return render(request, 'blog/Registro.html', context)


def afortunado_list(request):
    return render(request, 'blog/Afortunado.html')
def marlene_list(request):
    return render(request, 'blog/Marlene.html')
def okon_list(request):
    return render(request, 'blog/Okon.html')
def atacamita_list(request):
    return render(request, 'blog/Atacamita.html')
def login_list(request):
    return render(request, 'blog/login.html')
def mascota_list(request):
	mascotas = Mascota.objects.all().order_by('nombre')
	return render(request, 'blog/mascota_list.html', {'mascotas':mascotas})



def base_admin(request):
    return render(request, 'blog/baseAdmin.html')

def contacto(request):

    form = ContactForm(request.POST or None)

    context = {
        "form":form
    }
    if form.is_valid(): 
        form_data = form.cleaned_data
        name = form_data.get("nombres")
        email = form_data.get("email")
        mensj = form_data.get("mensaje")
        obj = Contacto.objects.create(nombre=name,
        email=email, 
        mensaje=mensj) 
       

    return render(request, 'blog/contacto.html',context)

def baselog(request):

    return render(request, 'blog/Baselog.html')

def baseListar(request):
    return render(request, 'blog/baseListar.html')

def campania(request):
    return render(request, 'blog/campania.html')