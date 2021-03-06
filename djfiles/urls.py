"""djfiles URL Configuration

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
from django.contrib import admin
from django.urls import path
from web import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('/', views.about, name="about"),
    path('about/', views.about, name="about"),
    path('test/', views.about, name="about"),
    path('kynan/', views.kynan, name="kynan"),
    path(':)/', views.secret, name="realsecret"),
    path('secret/', views.secret2, name="secret")
    #path('kynan/', views.nope, name="nope"),
    #path('about/', views.nope, name="nope"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
