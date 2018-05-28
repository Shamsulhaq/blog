"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name ='index'),
    path('article/<int:id>', views.singlepost, name ='single_post'),
    path('type/<name>', views.getcategory, name ='type'),
    path('login', views.getlogin, name ='login'),
    path('logout', views.getlogout, name ='logout'),
    path('signup', views.signup, name ='signup'),
    path('update_profile', views.profileupdate, name ='update_profile'),
    path('create_profile', views.profileCreate, name ='create_profile'),
    path('profile', views.getprofile, name ='profile'),
    path('create', views.aricle_create, name ='create'),
    path('update/<int:pid>', views.aricle_update, name ='update'),
    path('delete/<int:pid>', views.aricle_delete, name ='delete'),


]
