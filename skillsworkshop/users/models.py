
from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

User = AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    SKILLS_CHOICES = [
        ('AI & Robotics','AI & Robotics'),
        ('Business Analysis','Business Analysis'),
        ('Business Intelligence & Data Analytics','Business Intelligence & Data Analytics'),
        ('Business Transformation & Change','Business Transformation & Change'),
        ('Cloud & DevOps','Cloud & DevOps'),
        ('Design & Architecture','Design & Architecture'),
        ('Cyber Security','Cyber Security'),
        ('Digital, UX & UI design','Digital, UX & UI design'),
        ('ERP & CRM','ERP & CRM'),
        ('IT Support & Systems Administration','IT Support & Systems Administration'),
        ('Project Management','Project Management'),
        ('Software Development, Testing & Engineering','Software Development, Testing & Engineering'),
    ]
    INTEREST_CHOICES = [
        ('AI & Robotics','AI & Robotics'),
        ('Business Analysis','Business Analysis'),
        ('Business Intelligence & Data Analytics','Business Intelligence & Data Analytics'),
        ('Business Transformation & Change','Business Transformation & Change'),
        ('Cloud & DevOps','Cloud & DevOps'),
        ('Design & Architecture','Design & Architecture'),
        ('Cyber Security','Cyber Security'),
        ('Digital, UX & UI design','Digital, UX & UI design'),
        ('ERP & CRM','ERP & CRM'),
        ('IT Support & Systems Administration','IT Support & Systems Administration'),
        ('Project Management','Project Management'),
        ('Software Development, Testing & Engineering','Software Development, Testing & Engineering'),
    ]
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
    skills = MultiSelectField(choices = SKILLS_CHOICES)
    interest = MultiSelectField(choices = INTEREST_CHOICES)
    
    pass

    def __str__(self):
        return self.username
