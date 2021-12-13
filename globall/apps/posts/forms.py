from django import forms
from .models import Post
from apps.usuarios.models import Usuario



class Formulario_alta_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'categoria', 'video', 'imagen']
        exclude = ('usuario',)
    

