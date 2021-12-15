from django.urls import path 
from . import views

app_name = 'acerca'

urlpatterns = [
    
	path('acerca/', views.Acerca, name = 'acerca_nosotros'),
	path('ods/', views.Ods, name= 'las_ods')

]