from django.shortcuts import render

# Create your views here.
def home(request):
    # farmstand_data = Farm.objects.all()
    farmstand_data = { "farm_name": "Happy Valley",
                        "street_name": "123 Main St" }
    return render(request, 'frontend/index.html', { "farmstand_data": farmstand_data})
