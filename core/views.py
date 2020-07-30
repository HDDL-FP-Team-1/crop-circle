from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import FarmRegistrationForm
from .models import Tag, Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep, FarmQuerySet, search
from .forms import FarmAddressForm, CropForm, CustomerForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

def home_page(request):
    return render(request, "frontend/home.html")

def farm_create(request):
    if request.method == "POST":
        form = FarmAddressForm(data=request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user
            form.save()
            return redirect(to='home')
    else:
        form = FarmAddressForm()

    return render(request, 'frontend/farm.html', {'form': form})

def farm_detail(request, farm_pk):
    farm = get_object_or_404(Farm.objects.all(), pk=farm_pk)
    return render(request, 'frontend/farm_detail.html', {'farm': farm})

def farm_update(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    if request.method == 'POST':
        form = FarmForm(data=request.POST, instance=farm)
        if form.is_valid():
            farm = form.save()
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = FarmForm(instance=farm)

    return render(request, 'frontend/farm_update.html', {'form': form, 'farm': farm})

def farm_delete(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    if request.method == 'POST':
        farm.delete()
        return redirect(to='home')
    return render(request, 'frontend/farm_delete.html', {'farm': farm})

def crop_create(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    if request.method == 'POST':
        form = CropForm(data=request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farm = farm
            crop.save()
        
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = CropForm()
    return render(request, 'frontend/crop_create.html', {'form': form, 'farm': farm})
    
def crop_detail(request, crop_pk):
    crop = get_object_or_404(Crop.objects.all(), pk=crop_pk)
    return render(request, 'frontend/crop_detail.html', {'crop': crop})
    

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'frontend/crop_list.html', {'crops': crops})

def crop_update(request, crop_pk):
    crop = get_object_or_404(Crop.objects.all(), pk=crop_pk)
    if request.method == 'POST':
        form = CropForm(data=request.POST, instance=crop)
        if form.is_valid():
            crop = form.save()
            return redirect(to='crop_detail', crop_pk=crop.pk)
    else:
        form = CropForm(instance=crop)

    return render(request, 'frontend/crop_update.html', {'form': form, 'crop': crop})

def crop_delete(request, crop_pk):
    crop = get_object_or_404(Crop.objects.all(), pk=crop_pk)
    farm = crop.farm
    if request.method == 'POST':
        crop.delete()
        return redirect(to='farm_detail', farm_pk=farm.pk)
    return render(request, 'frontend/crop_delete.html', {'crop': crop})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            form.save()
            return redirect(to='home')
    else:
        form = CustomerForm()

    return render(request, 'frontend/customer_detail.html', {'form': form})
#need to create the views I lost
def customer_detail(request, customer_pk):
    profile = get_object_or_404(Customer.objects.all(), pk=customer_pk)
    return render(request, 'frontend/customer_detail.html', {'profile': profile})

def search_farms(request):
    query = request.GET.get("q")

    if query is not None:
        farms = search(query)
    else:
        farms = None

    return render(
        request, "frontend/search.html", {"farms": farms, "query": query or ""}
    )
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    success_url = reverse_lazy('farm_create')