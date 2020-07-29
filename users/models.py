from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# from core.models import Farm

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    farm = models.ForeignKey(to='core.Farm', on_delete=models.CASCADE, related_name='farms', null=True, blank=True)
    # customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name='customers', null=True, blank=True)
    first_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55, null=True, blank=True)
    farm = models.CharField(max_length=55, null=True, blank=True)


class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    photo = models.FileField()    
