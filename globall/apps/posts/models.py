from django.contrib import auth
from django.db import models
from django.conf import settings
from apps.usuarios.models import Usuario
from django.contrib.auth.models import User
# Create your models here.



class Categoria(models.Model):
	nombre = models.CharField(max_length = 30)
	descripcion = models.CharField(max_length = 200, null = False)

	def __str__(self):
		return self.nombre


class Post(models.Model):
	titulo = models.CharField(max_length = 30)
	descripcion = models.TextField(max_length = 400, null = False)
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
	video = models.CharField(max_length=300, null = True, blank=True)
	fecha = models.DateField(auto_now=False, auto_now_add=True, null=True)
	imagen = models.ImageField(upload_to = 'imagenes_post', null=True, blank=True)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)
	
	def __str__(self):
		return self.titulo

class Comentario(models.Model):
	descripcion = models.TextField(max_length = 1000, null = False)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)

	def __str__(self):
		return (self.descripcion)
