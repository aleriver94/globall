from django.urls import path
from . import views

app_name='posts'

urlpatterns = [

    path('posts/', views.MostrarPosts, name = 'mostrar_posts')
]