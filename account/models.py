from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=35)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username