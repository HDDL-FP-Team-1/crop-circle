from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    # farmstand_data = Farm.objects.all()
    farmstand_data = { "farm_name": "Happy Valley",
                        "street_name": "123 Main St" }
    return render(request, 'frontend/index.html', { "farmstand_data": farmstand_data})

def farmer_profile(request):
    if request.user.is_authenticated:
        # return redirect(to='frontend/farmerprofile')
    
        return render(request, "frontend/farmerprofile.html")

def logout(request):
    pass 

def login(request):
    return render (request, "accounts/login.html")
