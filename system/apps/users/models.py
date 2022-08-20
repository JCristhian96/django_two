from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ Modelo de usuarios """
    
    email = models.EmailField(unique=True, blank=False, null=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    