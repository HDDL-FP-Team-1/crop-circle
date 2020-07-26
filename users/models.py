from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    pass

class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    photo = models.FileField()    
