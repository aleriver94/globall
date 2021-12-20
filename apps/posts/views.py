from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post, Categoria, Comentario
from .forms import Formulario_alta_post, Formulario_alta_comentario
from apps.usuarios.models import Usuario
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
import datetime
import random

# Create your views here.

def MostrarPosts(request):

    posts_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 2)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render (request, 'posts/mostrarPosts.html', {'posts': posts})



    #ctx={}
    #ctx['post'] = p
    #ctx['titulo'] = "Hola soy la lista de posts"

    #return render(request,'posts/mostrarPosts.html', ctx)

def DetallePost(request,pk):

    p = Post.objects.get(pk = pk)
    ctx = {}
    ctx['post'] = p
    return render(request, 'posts/detallePost.html', ctx)


def MostrarComentarios(request, pk):

    post = Post.objects.get(pk=pk)

    p = Comentario.objects.filter(post=post)

    ctx={}
    ctx['comentarios'] = p

    return render(request, 'posts/mostrarComentarios.html', ctx)


class AltaPost(LoginRequiredMixin, CreateView):
    model = 'Post'
    template_name = 'posts/alta.html'
    form_class = Formulario_alta_post
    success_url = reverse_lazy('posts:mostrar_posts')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AltaComentario(LoginRequiredMixin, CreateView):
    model = 'Comentario'
    template_name = 'posts/alta_comentario.html'
    form_class = Formulario_alta_comentario

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        pk = self.kwargs['pk']
        #pasarobjeto post
        x = Post.objects.get(pk=pk)
        form.instance.post = x
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('posts:mostrar_comentario', kwargs={'pk':self.kwargs['pk']})

def FiltroxPersona(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['post'] = p

    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4

    return render(request, 'categorias/filtroXPersona.html', ctx)

def FiltroxPaz(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['post'] = p
    ctx['categoria'] = categoria
    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4

    return render(request, 'categorias/filtroXPaz.html', ctx)

def FiltroxPlaneta(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['post'] = p
    ctx['categoria'] = categoria
    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4
    return render(request, 'categorias/filtroXPlaneta.html', ctx)

def FiltroxProsperidad(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['post'] = p
    ctx['categoria'] = categoria
    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4
    return render(request, 'categorias/filtroXProsperidad.html', ctx)

def FiltroxAlianza(request, pk):
    categoria = Categoria.objects.get(pk=pk)

    p = Post.objects.filter(categoria = categoria)

    ctx = {}
    ctx['post'] = p
    ctx['categoria'] = categoria
    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4
    return render(request, 'categorias/filtroXAlianza.html', ctx)

def FiltroXFechaActual(request):

    list_post = Post.objects.filter(fecha=datetime.datetime.now())
    ctx = {}
    ctx['posts'] = list_post
    p2=Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4
    return render(request, 'posts/filtroXFechaActual.html', ctx)
