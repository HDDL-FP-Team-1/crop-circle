from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .models import Tag, Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep, FarmQuerySet, search, get_farms_for_user
from .forms import FarmAddressForm, CropForm, CustomerForm, FarmRegistrationForm, HourForm, OffSiteForm, FarmImageForm


from django.views.generic.edit import FormView
from registration.backends.simple.views import RegistrationView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    farms = Farm.objects.all()
    return render(request, "frontend/home.html", {'farms': farms})

def farm_create(request):
    if request.method == "POST":
        form = FarmAddressForm(data=request.POST, files=request.FILES)
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

    user_favorite_farm = False
    if request.user.is_authenticated:
        user_favorite_farm = request.user.is_favorite_farm(farm)

    if request.method == 'POST':
        form = CropForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farm = farm
            crop.save()
        
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = CropForm()

    return render(request, 'frontend/farm_detail.html', {'form': form, 'farm': farm})


def farm_list(request):
    farms = get_farms_for_user(Farm.objects, request.user)
    return render(request, 'frontend/farm_list.html', {'farms': farms})


def farm_update(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    if request.method == 'POST':
        form = FarmAddressForm(data=request.POST, files=request.FILES, instance=farm)
        if form.is_valid():
            farm = form.save()
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = FarmAddressForm(instance=farm)

    return render(request, 'frontend/farm_update.html', {'form': form, 'farm': farm})


def farm_delete(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    if request.method == 'POST':
        farm.delete()
        return redirect(to='home')
    return render(request, 'frontend/farm_delete.html', {'farm': farm})


def farm_image_add(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)   
    # image = farm.image.first()
    
    if request.method == 'POST':
        image_form = FarmImageForm(data=request.POST, files=request.FILES, instance=farm)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.farm = farm
            image.save()
        
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        image_form = FarmImageForm(instance=farm)
    
    return render(request, 'frontend/farm_image_add.html', {'image_form': image_form, 'farm': farm})

def crop_create(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    
    if request.method == 'POST':
        form = CropForm(data=request.POST, files=request.FILES)
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
        form = CropForm(data=request.POST, files=request.FILES, instance=crop)
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

def hour_create(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    hour = farm.hours.filter().first()
    if request.method == 'POST':
        form = HourForm(data=request.POST, files=request.FILES, instance=hour)
        if form.is_valid():
            hour = form.save(commit=False)
            hour.farm = farm
            hour.save()
        
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = HourForm()
    return render(request, 'frontend/hour_create.html', {'form': form, 'farm': farm})

def hour_update(request, farm_pk):
    farm = get_object_or_404(request.user.farms, pk=farm_pk)
    hour = farm.hours.filter().first()
    if request.method == 'POST':
        form = HourForm(data=request.POST, files=request.FILES, instance=hour)
        if form.is_valid():
            hour = form.save()
                    
            return redirect(to='farm_detail', farm_pk=farm.pk)
    else:
        form = HourForm()
    return render(request, 'frontend/hour_update.html', {'form': form, 'farm': farm})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            form.save()
            return redirect(to='home')
    else:
        form = CustomerForm()

    return render(request, 'frontend/customer_create.html', {'form': form})

def customer_detail(request, customer_pk):
    profile = get_object_or_404(Customer.objects.all(), pk=customer_pk)
    return render(request, 'frontend/customer_detail.html', {'profile': profile})

def customer_edit(request, customer_pk):
    customer = get_object_or_404(Customer.objects.all(), pk=customer_pk)
    
    if request.method == 'POST':
        form = CustomerForm(data=request.POST, files=request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(to='customer_detail', customer_pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'frontend/customer_edit.html', {'form': form, 'customer':customer})

def customer_delete(request, customer_pk):
    customer = get_object_or_404(Customer.objects.all(), pk=customer_pk)

    if request.method == 'POST':
        offsite.delete()
        return redirect(to='home')

    return render(request, 'frontend/customer_delete.html', {'customer': customer})

def offsite_create(request):
    if request.method == "POST":
        form = OffSiteForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            offsite = form.save(commit=False)
            offsite.user = request.user
            form.save()
            return redirect(to='offsite_detail', offsite_pk=offsite.pk)
    else:
        form = OffSiteForm()

    return render(request, 'frontend/offsite_create.html', {'form': form})

def offsite_detail(request, offsite_pk):
    offsite = get_object_or_404(OffSite.objects.all(), pk=offsite_pk)
    return render(request, 'frontend/offsite_detail.html', {'offsite': offsite})

def offsite_edit(request, offsite_pk):
    offsite = get_object_or_404(OffSite.objects.all(), pk=offsite_pk)
    
    if request.method == 'POST':
        form = OffSiteForm(data=request.POST, files=request.FILES, instance=offsite)
        if form.is_valid():
            form.save()
            return redirect(to='offsite_detail', offsite_pk=offsite.pk)
    else:
        form = OffSiteForm(instance=offsite)

    return render(request, 'frontend/offsite_edit.html', {'form': form, 'offsite':offsite})

def offsite_delete(request, offsite_pk):
    offsite = get_object_or_404(OffSite.objects.all(), pk=offsite_pk)

    if request.method == 'POST':
        offsite.delete()
        return redirect(to='home')

    return render(request, 'frontend/offsite_delete.html', {'offsite': offsite})
    
def registration_transfer(request):
    return render(request, "frontend/registration_transfer.html")

def search_farms(request):
    query = request.GET.get("q")

    if query is not None:
        farms = search(query)
    else:
        farms = None

    return render(
        request, "frontend/search.html", {"farms": farms, "query": query or ""}
    )

@csrf_exempt
def toggle_favorite_farm(request, farm_pk):
    farm = get_object_or_404(Farm.objects.all(), pk=farm_pk)

    if request.user.is_favorite_farm(farm):
        request.user.favorite_farms.remove(farm)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_farms.add(farm)
        return JsonResponse({"isFavorite": True})

class MyRegistrationView(RegistrationView):
    success_url = reverse_lazy('farm_create')

