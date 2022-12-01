"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from newsapp import views

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('contact', views.contact ,name='contact'),
    path('home', views.home ,name='home'),
    path('signup', views.handlesignup ,name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('sports', views.sports ,name='sports'),
    path('science', views.science ,name='science'),
    path('technology', views.technology ,name='technology'),
    path('health', views.health ,name='health'),
    path('general', views.general ,name='general'),
    path('entertainment', views.entertainment ,name='entertainment'),
    path('business', views.business ,name='business'),
    path('weather', views.weather ,name='weather'),
]
