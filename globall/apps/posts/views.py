from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post, Categoria, Comentario
from .forms import Formulario_alta_post
from apps.usuarios.models import Usuario

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

class AltaPost(CreateView):
    model = 'Post'
    template_name = 'posts/alta.html'
    form_class = Formulario_alta_post
    success_url = reverse_lazy('posts:mostrar_posts')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)