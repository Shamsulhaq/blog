from django.views import View
from django.shortcuts import render,get_object_or_404 ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout
from .forms import SignUpForm
from . import models
from django.db.models import Q

# Create your views here.

def index(request):

        post = models.Article.objects.all()

        search = request.GET.get('q')

        if search:
            post = models.Article.objects.filter(
                Q (title__icontains=search)|
                Q (details__icontains=search))


        posts = {
            'posts': post
        }

        return render(request, 'index.html', posts)

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

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get("username")
            password = request.POST.get("pwd")

            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')


    return render(request,'login.html')

def getlogout (request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})