"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^Registro', views.registrar_list),
    url(r'^Afortunado', views.afortunado_list),
    url(r'^Atacamita', views.atacamita_list),
    url(r'^Marlene', views.marlene_list),
    url(r'^Okon', views.okon_list),
    url(r'^Mascota', views.mascota_list),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/',
    TemplateView.as_view(template_name='blog/profile.html'),
    name='profile'),
    url(r'^Contacto', views.contacto), 
    url(r'^Loggg',views.baselog),
    url(r'^baseAdmin', views.base_admin),
    url(r'^baseListar', views.baseListar),
    url(r'^Base', views.base_list),
    url(r'^Campania', views.campania)
]

    