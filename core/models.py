from django.db import models
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from ordered_model.models import OrderedModel
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
from users.models import User
import datetime as dt


class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag



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
    # hours = models.ManyToManyField(to=OpenHours, related_name="hours")
    image = models.ImageField(default='default.jpg', upload_to='images')
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='farms', blank=True)
    about_us = models.TextField(max_length=1500, null=True, blank=True)
<<<<<<< HEAD
    favorited_by = models.ManyToManyField(to=User, related_name='favorite_farms', blank=True)
=======

    def __str__(self):
        return self.name

class OpenHours(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='hours', null=True, blank=True)
    mon_start = models.TimeField(verbose_name='Monday Opening Time', null=True, blank=True, default=None)
    mon_end = models.TimeField(verbose_name='Monday Closing Time', null=True, blank=True, default=None)
    tue_start = models.TimeField(verbose_name='Tuesday Opening Time', null=True, blank=True, default=None)
    tue_end = models.TimeField(verbose_name='Tuesday Closing Time',null=True, blank=True, default=None)
    wed_start = models.TimeField(verbose_name='Wednesday Opening Time',null=True, blank=True, default=None)
    wed_end = models.TimeField(verbose_name='Wednesday Closing Time',null=True, blank=True, default=None)
    thu_start = models.TimeField(verbose_name='Thursday Opening Time',null=True, blank=True, default=None)
    thu_end = models.TimeField(verbose_name='Thursday Closing Time',null=True, blank=True, default=None)
    fri_start = models.TimeField(verbose_name='Friday Opening Time',null=True, blank=True, default=None)
    fri_end = models.TimeField(verbose_name='Friday Closing Time',null=True, blank=True, default=None)
    sat_start = models.TimeField(verbose_name='Saturday Opening Time',null=True, blank=True, default=None)
    sat_end = models.TimeField(verbose_name='Saturday Closing Time',null=True, blank=True, default=None)
    sun_start = models.TimeField(verbose_name='Sunday Opening Time',null=True, blank=True, default=None)
    sun_end = models.TimeField(verbose_name='Sunday Closing Time',null=True, blank=True, default=None)


class OffSite(models.Model):
    pass

class Crop(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='crops', null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item
>>>>>>> master

class Customer(models.Model):
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customers', null=True)
    avatar = models.ImageField(default='default.jpg', upload_to='images')
    street_address = models.CharField(verbose_name='Street Address', max_length=255, null=True, blank=True)
    street_address_line_2 = models.CharField(verbose_name='Street Address Line 2', max_length=255, null=True, blank=True)
    city = models.CharField(verbose_name='City', max_length=255, null=True, blank=True)
    state = models.CharField(verbose_name='State', max_length=255, null=True, blank=True)
    zip_code = models.CharField(verbose_name='Zip', max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    web_link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

class OffSite(models.Model):
    pass

class Crop(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='crops', null=True, blank=True)
    item = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.item

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