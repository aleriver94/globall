from random import random
from django.shortcuts import render
from apps import posts
import random
from django.contrib.auth.decorators import login_required

def index(request):

    p=posts.models.Post.objects.all()
    a = random.choice(p)
    ctx={}
    ctx['post'] = a
    p2=posts.models.Post.objects.all()
    a2= random.choice(p2)
    a3= random.choice(p2)
    a4= random.choice(p2)
    ctx['lateral']=a2
    ctx['lateral2']=a3
    ctx['lateral3']=a4
    return render (request, 'index.html', ctx)