from django.db import models

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

def __str__(self):
	return self.titulo

class Comentario(models.Model):
	descripcion = models.TextField(max_length = 1000, null = False)
	Post = models.ForeignKey(Post, on_delete = models.CASCADE)

def __str__(self):
	return self.descripcion
