
from django.db import models
from django.contrib.auth.models import AbstractUser

User = AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=200, blank=True)
    profile_picture = models.URLField(blank=True)
    is_mentor = models.BooleanField(default=False)
    is_mentee = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)
    
    
    pass

    def __str__(self):
        return self.username
