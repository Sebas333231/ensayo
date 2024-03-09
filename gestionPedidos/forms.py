from django import forms



class FormularioContacto(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    comentario = forms.CharField()