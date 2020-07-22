from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Tag, Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep
from django.views.generic import View, TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView


def home_page(request):
    return render(request, "home.html")

class FarmCreateView(CreateView):
    model = Farm
    fields = [
        'user',
        'name',
        'image',
        'location',
        'website',
    ]

class FarmDetailView(DetailView):
    model = Farm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_updated'] = timezone.now()
        return context

class FarmUpdateView(UpdateView):
    model = Farm
    fields = [
        'user',
        'name',
        'image',
        'location',
        'website',
    ]
    #quality check url
    success_url ="/<farm_pk>/"

class FarmDeleteView(DeleteView):
    model = Farm
    success_url = reverse_lazy('farm-list')

class CropCreateView(CreateView):
    model = Crop
    fields = ['item']

class CropListView(ListView):
    pass

class CropUpdateView(UpdateView):
    pass

class CropDeleteView(DeleteView):
    model = Crop
    success_url = reverse_lazy('crop-list')

class OffSiteCreateView(CreateView):
    model = OffSite
    fields = [
        'crop',
        'location',
    ]

class OffSiteDetailView(DetailView):
    pass

class OffSiteUpdateView(UpdateView):
    pass

class OffSiteDeleteView(DeleteView):
    model = OffSite
    success_url = reverse_lazy('farm-detail')

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['user', 'avatar']

class CustomerDetailView(DetailView):
    pass

class CustomerUpdateView(UpdateView):
    pass

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('home')

class RecipeCreateView(CreateView):
    model = Recipe
    fields = [
        'title',
        'prep_time',
        'cook_time',
    ]

class RecipeDetailView(DetailView):
    pass

class RecipeUpdateView(UpdateView):
    pass

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-list')

class SearchListView(ListView):
    pass