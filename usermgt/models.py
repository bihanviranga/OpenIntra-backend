from django.db import models
from django.contrib.auth.models import AbstractUser

"""
Inherits:
    username
    password
    first_name
    last_name
    email
    date_joined
"""
class User(AbstractUser):
    role = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

