from django.db import models
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
#     offsite = models.ForeignKey(to=Offsite, null=True, blank=True)
#     farm = models.ForeignKey(to=Farm, null=True, blank=True)
#     weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
#     from_hour = models.TimeField()
#     to_hour = models.TimeField()

class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

class Farm(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='farmers')
    name = models.CharField(max_length=255)
    location = LocationField()
    address = AddressAutoHiddenField()
    website = models.CharField(max_length=255, null=True, blank=True)
    
class Crop(models.Model):
    pass
    # farm = models.ForeignKey(to=Farm)
    # item_name = models.TextField
    

class Offsite(models.Model):
    farm = models.ForeignKey(to=Farm, on_delete=models.CASCADE, related_name='offsites')
    crop = models.ForeignKey(to=Crop, on_delete=models.CASCADE, related_name='offsites')
    location = LocationField()
    address = AddressAutoHiddenField()
    
class Customer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='customers')
    avatar = models.ImageField(default='default.jpg', upload_to='images')

class Recipe(models.Model):
    pass

class Ingredient(models.Model):
    pass

class RecipeStep(models.Model):
    pass


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