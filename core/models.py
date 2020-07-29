from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from ordered_model.models import OrderedModel
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
from users.models import User


class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='farms', null=True, blank=True)
    name = models.CharField(max_length=255)
    # crop = models.ManyToManyField(to=Crop, related_name='farm_crops')
    # location = LocationField(map_attrs={"center": [0,0], "marker_color": "blue", "track_location_button": True, "geocoder": True}, null=True, blank=True, default='')    
    street_address = models.CharField(verbose_name='Street Address', max_length=255, null=True, blank=True)
    street_address_line_2 = models.CharField(verbose_name='Street Address Line 2', max_length=255, null=True, blank=True)
    city = models.CharField(verbose_name='City', max_length=255, null=True, blank=True)
    state = models.CharField(verbose_name='State', max_length=255, null=True, blank=True)
    zip_code = models.CharField(verbose_name='Zip', max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    hours = models.ManyToManyField(to=OpenHours, related_name="hours")
    image = models.ImageField(default='default.jpg', upload_to='images')
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='farms', blank=True)

    def __str__(self):
        return self.name

class OffSite(models.Model):
    pass
#     farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='OffSites')
#     # crop = models.ManyToManyField(to=Crop, related_name='offsite_crops')
#     location = LocationField(map_attrs={"center": [0,0], "marker_color": "blue", "track_location_button": True, "geocoder": True}, null=True, blank=True, default='')    
#     address = models.CharField(max_length=255, null=True, blank=True)
#     hours = models.ManyToManyField(to=OpenHours, related_name="offsite_hours")

# class Place(models.Model):
#     farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='crops', null=True, blank=True)
#     offsite = models.ForeignKey(to=OffSite, on_delete=models.CASCADE, related_name='offsite_crops', null=True, blank=True)
#     location = LocationField(
#         map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": (17.031645, 51.106715)})
#     created_at = models.DateTimeField(auto_now_add=True)

class Crop(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
    # offsite = models.ForeignKey(to=OffSite, on_delete=models.CASCADE, related_name='offsite_locations', null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item


class Customer(models.Model):
    customer = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='customers', null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='images')

class Recipe(models.Model):
    author = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='recipes', null=True)
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

def search(search_term):
    farms = Farm.objects.all()
    return farms \
        .annotate(search=SearchVector("name", "crops__item", "OffSites", "tags__tag")) \
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