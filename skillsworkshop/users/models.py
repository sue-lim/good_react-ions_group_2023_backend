
from django.db import models
from django.contrib.auth.models import AbstractUser

User = AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    bio = models.TextField()
    phone_number = models.IntegerField()
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=200)
    profile_picture = models.URLField()
    is_mentor = models.BooleanField()
    is_mentee = models.BooleanField(default=True)
    is_private = models.BooleanField()
    
    
    pass

    def __str__(self):
        return self.username
