"""StreamStation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from streamit import views as streamit_views

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', streamit_views.StreamView.as_view()),
    url(r'^on_publish$', streamit_views.on_publish),
    url(r'^on_publish_done$', streamit_views.on_publish_done),
]
