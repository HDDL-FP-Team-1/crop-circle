from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Tag, Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep, FarmQuerySet, search
from django.views.generic import View, TemplateView, CreateView, DeleteView, UpdateView, ListView, DetailView


def home_page(request):
    return render(request, "home.html")

class FarmCreateView(CreateView):
    model = Farm
    template_name = 'frontend/farm.html'
    fields = [
        'user',
        'name',
        'website',
        'location',
        'image',
    ]

    success_url = reverse_lazy('farm')

class FarmDetailView(DetailView):
    model = Farm
    template_name = 'frontend/farm_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_updated'] = timezone.now()
        return context

class FarmUpdateView(UpdateView):
    model = Farm
    fields = [
    #quality check url
        'name',
        'image',
        'location',
        'website',
    ]

class FarmDeleteView(DeleteView):
    model = Farm
    success_url = reverse_lazy('home')

class CropCreateView(CreateView):
    model = Crop
    template_name = 'frontend/crop.html'
    fields = ['item']

    success_url = reverse_lazy('crop_list')

class CropDetailView(DetailView):
    model = Crop
    template_name = 'frontend/crop_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CropListView(ListView):
    model = Crop
    template_name = 'frontend/crop_list.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CropUpdateView(UpdateView):
    model = Crop
    template_name = 'frontend/crop_update.html'
    fields = [
        'item'
    ]
    success_url = reverse_lazy('crop_list')

class CropDeleteView(DeleteView):
    model = Crop
    template_name = 'frontend/crop_delete.html'
    success_url = reverse_lazy('crop_list')

class OffSiteCreateView(CreateView):
    model = OffSite
    fields = [
        # 'location',
        'crops'
    ]
    success_url = reverse_lazy('farm')

class OffSiteDetailView(DetailView):
    model = OffSite
    template_name = 'frontend/offsite_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class OffSiteUpdateView(UpdateView):
    model = OffSite
    template_name = 'frontend/offsite_update.html'
    fields = [
        # 'location',
        'crops'
    ]

class OffSiteDeleteView(DeleteView):
    model = OffSite
    success_url = reverse_lazy('farm_detail')

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['user', 'avatar']
    success_url = reverse_lazy('home')

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'frontend/customer_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CustomerUpdateView(UpdateView):
    
    model = Customer
    fields = ['user', 
        'avatar'
    ]
    success_url = reverse_lazy('customer_detail')

class CustomerDeleteView(DeleteView):
    
    model = Customer
    success_url = reverse_lazy('home')

class RecipeCreateView(CreateView):
    
    model = Recipe
    template_name = 'frontend/recipe_create.html'
    
    fields = [
        'title',
        'prep_time',
        'cook_time',
    ]

    success_url = reverse_lazy('recipe_detail')

class RecipeDetailView(DetailView):
    
    model = Recipe
    template_name = 'frontend/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RecipeListView(ListView):
    
    model = Recipe
    template_name = 'frontend/recipe_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RecipeUpdateView(UpdateView):
    
    model = Recipe
    template_name = 'frontend/recipe_update.html'
    
    fields = [
        'title',
        'prep_time',
        'cook_time',
    ]
    
    success_url = reverse_lazy('recipe_list')

class RecipeDeleteView(DeleteView):
    
    model = Recipe
    success_url = reverse_lazy('recipe_list')

class IngredientCreateView(CreateView):
    
    model = Ingredient
    template_name = 'frontend/ingredient_create.html'
    
    fields = [
        'item',
        'amount',
    ]

    success_url = reverse_lazy('recipe_detail')

class IngredientUpdateView(UpdateView):
    
    model = Ingredient
    template_name = 'frontend/ingredient_update.html'
    
    fields = [
        'item',
        'amount',
    ]

class IngredientDeleteView(DeleteView):
    
    model = Ingredient
    success_url = reverse_lazy('recipe_detail')

class RecipeStepCreateView(CreateView):
    
    model = RecipeStep
    template_name = 'frontend/add_recipestep.html'
    
    fields = [
        'text',
    ]

    success_url = reverse_lazy('recipe_detail')

class RecipeStepUpdateView(UpdateView):
    
    model = RecipeStep
    template_name = 'frontend/recipestep_update.html'
    
    fields = [
        'text',
    ]

class RecipeStepDeleteView(DeleteView):
    
    model = RecipeStep
    success_url = reverse_lazy('recipe_detail')

# class SearchListView(ListView):
#     pass



def search_farms(request):
    query = request.GET.get("q")

    if query is not None:
        farms = search(query)
    else:
        farms = None

    return render(
        request, "frontend/search.html", {"farms": farms, "query": query or ""}
    )
