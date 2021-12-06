from django.shortcuts import render

# Create your views here.

def MostrarPosts(request):

    return render(request,'posts/mostrarPosts.html')