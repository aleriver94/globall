from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def Acerca(request):

	return render(request,'acerca/acerca.html')

def Ods(request):

	return render(request,'acerca/ods.html')