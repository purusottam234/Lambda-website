"""lambda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include
from app.views import Register, home,businesslist,packages, seo,searchposts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"),name='register-success'),
    path('register/',Register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('',home),
    path('package-list/',packages,name='packagelist'),
    path('seo-list/',seo,name='seolist'),
    path('business-list/',businesslist,name='createlist'),
    path('business-list/search/', searchposts, name='searchposts'),
     


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
