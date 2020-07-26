from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from ordered_model.models import OrderedModel
from users.models import User
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

class Crop(models.Model):
    item = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item
    # integrate API on the front-end in order to build database entries of crops

WEEKDAYS = (
  (1, "Monday"),
  (2, "Tuesday"),
  (3, "Wednesday"),
  (4, "Thursday"),
  (5, "Friday"),
  (6, "Saturday"),
  (7, "Sunday"),
)

class OpenHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ('weekday', 'from_hour')
        unique_together = ('weekday', 'from_hour', 'to_hour')

    def __str__(self):
        return f'{self.get_weekday_display()} : {self.from_hour} - {self.to_hour}'

class Farm(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='farmers', null=True, blank=True)
    name = models.CharField(max_length=255)
    crop = models.ManyToManyField(to=Crop, related_name='farm_crops')
    location = LocationField(null=True)
    address = AddressAutoHiddenField(null=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    hours = models.ManyToManyField(to=OpenHours, related_name="hours")
    image = models.ImageField(default='default.jpg', upload_to='images')
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='farms')

    def __str__(self):
        return self.name

class OffSite(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='OffSites')
    crop = models.ManyToManyField(to=Crop, related_name='offsite_crops')
    location = LocationField()
    address = AddressAutoHiddenField()
    hours = models.ManyToManyField(to=OpenHours, related_name="offsite_hours")
    


class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customers')
    avatar = models.ImageField(default='default.jpg', upload_to='images')

class Recipe(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=255, null=True)
    prep_time = models.PositiveIntegerField(null=True, blank=True)
    cook_time = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='recipes')

    #add tag funtions
    #add function for total cook time

class Ingredient(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='ingredient', null=True)
    amount = models.CharField(max_length=20, null=True)
    item = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.amount} {self.item}"
        
class RecipeStep(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='steps', null=True)
    text = models.TextField(null=True)
    # order_with_respect_to = "recipe"

    # def __str__(self):
    #     return f"{self.order} {self.text}"

class FarmQuerySet(models.QuerySet):
    def get_farms(self):
        farms = Farm.objects.all()
        return farms

    # def search(self, search_term):
    #     farms = self.annotate(
    #         search=SearchVector(
    #             "name", "OffSites", "tags__tag"
    #         )
    #     )
    #     farms = farms.filter(search=search_term).distinct("pk")
    #     return farms

def search(search_term):
    farms = Farm.objects.all()
    return farms \
        .annotate(search=SearchVector("name", "crop", "OffSites", "tags__tag")) \
        .filter(search=search_term) \
        .distinct('pk')

# Tag functions
    # def get_tag_names(self):
    #     tag_names = []
    #     for tag in self.tags.all():
    #         tag_names.append(tag.tag)

    #     return " ".join(tag_names)

    # def set_tag_names(self, tag_names):
    #     tag_names = tag_names.split()
    #     tags = []
    #     for tag_name in tag_names:
    #         tag = Tag.objects.filter(tag=tag_name).first()
    #         if tag is None:
    #             tag = Tag.objects.create(tag=tag_name)
    #         tags.append(tag)
    #     self.tags.set(tags)

    # hours = models.ForignKey(OpeningHours, on_delete=models.CASCADE, related_name='farms')