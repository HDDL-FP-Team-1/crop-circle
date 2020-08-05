from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    farm = models.ForeignKey(to='core.Farm', on_delete=models.CASCADE, related_name='farms', null=True, blank=True)
    # customer = models.ForeignKey(to='core.Customer', on_delete=models.CASCADE, related_name='customers', null=True, blank=True)
    first_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55, null=True, blank=True)

    # def is_favorite_farm(self, farm):
    #     return self.favorite_farms.filter(pk=farm.pk).count() == 1


class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    photo = models.ImageField()    

    def __str__(self):
        return self.uuid
