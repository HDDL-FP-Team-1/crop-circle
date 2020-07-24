from django.db import models
from ordered_model.models import OrderedModel
from users.models import User
from mapbox_location_field.models import LocationField, AddressAutoHiddenField

# class OpeningHours(models.Model):
#     WEEKDAYS = [
#     (1, _("Monday")),
#     (2, _("Tuesday")),
#     (3, _("Wednesday")),
#     (4, _("Thursday")),
#     (5, _("Friday")),
#     (6, _("Saturday")),
#     (7, _("Sunday")),
#     ]
#     OffSite = models.ForeignKey(to=OffSite, null=True, blank=True)
#     farm = models.ForeignKey(to=Farm, null=True, blank=True)
#     weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
#     from_hour = models.TimeField()
#     to_hour = models.TimeField()

class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

class Farm(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='farmers', null=True)
    name = models.CharField(max_length=255)
    location = LocationField()
    address = AddressAutoHiddenField()
    website = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='images')
    last_updated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='farms')
    
class Crop(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='crops', null=True)
    item = models.CharField(max_length=255, null=True, blank=True)
    # integrate API on the front-end in order to build database entries of crops

class OffSite(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='OffSites')
    crop = models.ManyToManyField(to=Crop, related_name='offsite_crops')
    location = LocationField()
    address = AddressAutoHiddenField()
    
class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customers')
    avatar = models.ImageField(default='default.jpg', upload_to='images')

class Recipe(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='recipes', null=True)
    title = models.CharField(max_length=255, null=True)
    prep_time = models.PositiveIntegerField(null=True, blank=True)
    cook_time = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='recipes', null=True, blank=True)

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