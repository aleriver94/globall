from django.shortcuts import render

# Create your views here.

def Acerca(request):

	return render(request,'acerca/acerca.html')
	