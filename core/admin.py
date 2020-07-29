from django.contrib import admin
from .models import Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep, OpenHours

admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(OffSite)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeStep)
admin.site.register(OpenHours)
# admin.site.register(Place)


