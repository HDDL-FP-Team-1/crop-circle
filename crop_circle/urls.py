"""crop_circle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from core import views as core_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home_page, name="home"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', TemplateView.as_view(template_name='frontend/index.html')),
    path('', core_views.home_page, name='home'),
    path('farm/add/', core_views.farm_create, name='farm_create'),
    path('farm/<int:farm_pk>/', core_views.farm_detail, name='farm_detail'),
    path('farm/<int:farm_pk>/update/', core_views.farm_update, name='farm_update'),
    path('farm/<int:farm_pk>/delete/', core_views.farm_delete, name='farm_delete'),
    path('farm/<int:farm_pk>/crop/add/', core_views.crop_create, name='crop_create'),
    path('crop/<int:crop_pk>/', core_views.crop_detail, name='crop_detail'),
    path('crop/list/', core_views.crop_list, name='crop_list'),
    path('crop/<int:crop_pk>/update/', core_views.crop_update, name='crop_update'),
    path('crop/<int:crop_pk>/delete/', core_views.crop_delete, name='crop_delete'),
    path('customer/add/', core_views.customer_create, name='customer_create'),
    path('customer/<int:customer_pk>/', core_views.customer_detail, name='customer_detail'),
    path('search/', core_views.search_farms, name='search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
