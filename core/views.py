from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    # farmstand_data = Farm.objects.all()
    farmstand_data = { "farm_name": "Happy Valley",
                        "street_name": "123 Main St" }
    return render(request, 'frontend/base.html', { "farmstand_data": farmstand_data})

def farmer_profile(request):
    if request.user.is_authenticated:
        return redirect(to='farmerprofile')
    
    return render(request, "crop_circle/farmerprofile.html")

def logout(request):
    pass 