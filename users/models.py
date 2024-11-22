from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/5m/%d/',blank=True,null=True,verbose_name='Фото')
    date_birth = models.DateTimeField(blank=True,null=True,verbose_name='Дата рождения')