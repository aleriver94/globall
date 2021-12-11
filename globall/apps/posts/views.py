from django.shortcuts import render
from .models import Post, Categoria, Comentario

# Create your views here.

def MostrarPosts(request):

    p = Post.objects.all()

    ctx={}
    ctx['post'] = p
    ctx['titulo'] = "Hola soy la lista de posts"

    return render(request,'posts/mostrarPosts.html', ctx)

def MostrarComentarios(request, pk):

    post = Post.objects.get(pk=pk)

    p = Comentario.objects.filter(post=post)

    ctx={}
    ctx['comentarios'] = p

    return render(request, 'posts/mostrarComentarios.html', ctx)