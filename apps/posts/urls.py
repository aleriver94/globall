from django.urls import path
from . import views

app_name='posts'

urlpatterns = [

    path('posts/', views.MostrarPosts, name = 'mostrar_posts'),

    path('mostrar/<int:pk>', views.MostrarComentarios, name='mostrar_comentario'),

    path('Alta/', views.AltaPost.as_view(), name="alta_post"),

    path('AltaC/<int:pk>', views.AltaComentario.as_view(), name="alta_comentario"),

    path('detallepost/<int:pk>', views.DetallePost, name ='detalle'),

    path('filtroPersona/<int:pk>', views.FiltroxPersona, name = 'filtroPersona'),

    path('filtroPaz/<int:pk>', views.FiltroxPaz, name = 'filtroPaz'),

    path('filtroPlaneta/<int:pk>', views.FiltroxPlaneta, name = 'filtroPlaneta'),

    path('filtroProsperidad/<int:pk>', views.FiltroxProsperidad, name = 'filtroProsperidad'),

    path('filtroAlianza/<int:pk>', views.FiltroxAlianza, name = 'filtroAlianza'),

    path('filtroFechaHoy/', views.FiltroXFechaActual, name = 'filtroFechaActual'),

]