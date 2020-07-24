from django.contrib import admin
from .models import Farm, Crop, OffSite, Customer, Recipe, Ingredient, RecipeStep

admin.site.register(Farm)
admin.site.register(Crop)
admin.site.register(OffSite)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeStep)

