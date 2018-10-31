from django.contrib import admin
from .models import Registrado, Mascota, Contacto


class MascotaRegistrado(admin.ModelAdmin):
    list_display = ["__str__", "nombre","foto","raza","descripcion","estado"]
    class meta:
        model = Mascota




admin.site.register(Registrado)
admin.site.register(Mascota)
admin.site.register(Contacto)

