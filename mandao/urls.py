"""mandao URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from apps.mdauth.decrators import cc_staff_required
from apps.mdmain import views
from . import views as mandao_views

urlpatterns = [
    path("a/",mandao_views.test),
    path("admin/", admin.site.urls),
    path('', views.index, name="index"),
    path('map/', include('apps.map.urls','map')),
    path('auth/', include('apps.mdauth.urls','mdauth')),
    path('mdmain/', include('apps.mdmain.urls','mdmain')),
    path('cms/',include('apps.cms.urls','cms')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
