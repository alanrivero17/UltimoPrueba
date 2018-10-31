from django import forms
from .models import Registrado, Mascota


class RegForm(forms.Form):

    email = forms.CharField(max_length=100)
    nombre_ = forms.CharField(max_length=100)
    rut = forms.CharField()
    telefono = forms.IntegerField()
    fechaNacimiento = forms.DateField()
    calle = forms.CharField(max_length=100,)
    numero_calle = forms.CharField(max_length=100)


class ContactForm(forms.Form):
    nombres = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre','size': '80'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese email','size': '80'}))
    mensaje =forms.CharField( widget = forms.Textarea(attrs={'placeholder': 'Ingrese mensaje'}))