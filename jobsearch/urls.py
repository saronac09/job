"""jobsearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path
from job.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base,name="home"),
    path('register/',reg,name="register"),
    path('login/',login,name="login"),
    path('headreg/',head,name="head"),
    path('userreg/',user,name="user"),
    path('empreg/',employeereg,name="empreg"),
    path('headhome/',headhome,name="headhome"),
    path('userlogin/',userlogin,name="userlogin"),
    path('userhome/',userhome,name="userhome"),
    path('headview/',headview,name="headview"),
    path('reqform/<id>',reqform,name="reqform"),
    path('req/',req,name="req"),
    path('adlogin/',adlogin,name="adlogin"),
    path('adminhome/',adminhome,name="adminhome"),
    path('userview/',userview,name="userview"),
    path('employeview/',employeview,name="employeview"),
]
