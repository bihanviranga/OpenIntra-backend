from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Inherited fields from AbstractUser:
        username
        password
        first_name
        last_name
        email
        date_joined
    """
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    # use the email field to login
    USERNAME_FIELD = 'email'
    # by default, USERNAME_FIELD and password is required
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return "{}".format(self.email)
