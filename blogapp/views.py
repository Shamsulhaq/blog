from django.views import View
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    post = models.Article.objects.all()

    posts = {
        'posts':post
    }

    return render(request,'index.html',posts)

def singlepost(request,id):

    post = get_object_or_404(models.Article,pk = id)
    related = models.Article.objects.filter( category = post.category ).exclude(id =id)[:4]

    context = { 'post':post, 'related':related}

    return render(request,'single.html',context)

def getcategory(request,name):

    cat = get_object_or_404(models.Category, name=name)
    post = models.Article.objects.filter(category =cat.id)
    context = {'posts': post ,'category':cat.name}
    return render(request,'category.html',context)
