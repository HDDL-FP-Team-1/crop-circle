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
    name = models.CharField(max_length=255, verbose_name='Farm Name') 
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

class Crop(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='crops', null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item

class Customer(models.Model):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customers', null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='images')

class Recipe(models.Model):
    author = models.ForeignKey(to='users.User', on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=255, null=True)
    prep_time = models.PositiveIntegerField(null=True, blank=True)
    cook_time = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='recipes')


class Ingredient(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='ingredient', null=True)
    amount = models.CharField(max_length=20, null=True)
    item = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.amount} {self.item}"
        
class RecipeStep(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE, related_name='steps', null=True)
    text = models.TextField(null=True)

class FarmQuerySet(models.QuerySet):
    def get_farms(self):
        farms = Farm.objects.all()
        return farms

def search(search_term):
    farms = Farm.objects.all()
    return farms \
        .annotate(search=SearchVector("name", "crops__item")) \
        .filter(search=search_term) \
        .distinct('pk')

def get_farms_for_user(queryset, user):
    if user.is_authenticated:
        farms = queryset.filter(Q(user=user))
    return farms