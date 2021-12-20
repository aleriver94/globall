from django import forms
from .models import Comentario, Post
from apps.usuarios.models import Usuario



class Formulario_alta_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'categoria', 'video', 'imagen']
        exclude = ('usuario',)
    

class Formulario_alta_comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields= ['descripcion']
        exclude = ('usuario',)