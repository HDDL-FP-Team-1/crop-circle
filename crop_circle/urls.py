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
from core.views import FarmCreateView, FarmDeleteView, FarmDetailView, FarmUpdateView, OffSiteCreateView, OffSiteDeleteView, OffSiteDetailView, OffSiteUpdateView, CropCreateView, CropDetailView, CropDeleteView, CropListView, CropUpdateView, CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerUpdateView, RecipeCreateView, RecipeDeleteView, RecipeDetailView, RecipeUpdateView, RecipeListView, IngredientCreateView, IngredientUpdateView, RecipeStepCreateView, RecipeStepUpdateView, RecipeStepDeleteView, IngredientDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', core_views.home, name="home"),
    # path('farmerprofile/', core_views.farmer_profile, name='farmerprofile'),
    # path('logout/', core_views.logout, name='logout'),
    # path('accounts/login/', core_views.login, name='login'),
    # path('accounts/homepage/', core_views.homepage, name='homepage'),
    # path('produce/', core_views.produce, name='produce'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', TemplateView.as_view(template_name='frontend/index.html')),
    path('', core_views.home_page, name='home'),
    path('farm/add/', FarmCreateView.as_view(), name='farm_create'),
    path('farm/<pk>/', FarmDetailView.as_view(), name='farm_detail'),
    path('farm/<pk>/update/', FarmUpdateView.as_view(), name='farm_update'),
    path('farm/<pk>/delete/', FarmDeleteView.as_view(), name='farm_delete'),
    path('offsite/add/', OffSiteCreateView.as_view(), name='offsite_create'),
    path('offsite/<pk>/', OffSiteDetailView.as_view(), name='offsite'),
    path('offsite/<pk>/update/', OffSiteUpdateView.as_view(), name='offsite_update'),
    path('offsite/<pk>/delete/', OffSiteDeleteView.as_view(), name='offsite_delete'),
    path('crop/add/', CropCreateView.as_view(), name='crop_create'),
    path('crop/<pk>/detail/', CropDetailView.as_view(), name='crop_info'),
    path('crop/list/', CropListView.as_view(), name='crop_list'),
    path('crop/<pk>/update/', CropUpdateView.as_view(), name='crop_update'),
    path('crop/<pk>/delete/', CropDeleteView.as_view(), name='crop_delete'),
    path('customer/add/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<customer_pk>/', CustomerDetailView.as_view(), name='customer'),
    path('customer/<customer_pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<customer_pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<pk>/detail/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<pk>/update/', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<pk>/delete/', RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/<pk>/add_ingredient/', IngredientCreateView.as_view(), name='add_ingredient'),
    path('recipe/<pk>/update_ingredient/', IngredientUpdateView.as_view(), name='ingredient_update'),
    path('recipe/<pk>/delete_ingredient/', IngredientDeleteView.as_view(), name='ingredient_delete'),
    path('recipe/<pk>/add_recipestep/', RecipeStepCreateView.as_view(), name='add_recipestep'),
    path('recipe/<pk>/update_recipestep/', RecipeStepUpdateView.as_view(), name='recipestep_update'),
    path('recipe/<pk>/delete_recipestep/', RecipeStepDeleteView.as_view(), name='recipestep_delete'),
    path('search/', core_views.search_farms, name='search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
