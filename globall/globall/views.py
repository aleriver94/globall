from random import random
from django.shortcuts import render
from apps import posts
import random

def index(request):

    p=posts.models.Post.objects.all()
    a = random.choice(p)
    ctx={}
    ctx['post'] = a

    return render (request, 'index.html', ctx)