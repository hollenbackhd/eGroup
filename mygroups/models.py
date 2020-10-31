from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import revers

class Mygroups(models.Model):
    def __str__(self):
        retrun self.title
    def get_absolute_url(self):
        return reverse('mygroups_detail', args=[str(self.id)])

# Create your models here.
