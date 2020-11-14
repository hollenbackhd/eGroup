from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.db.models import CharField, Model
from django_mysql.models import ListCharField

class Allgroups(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    discussion = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('allgroups_detail', args=[str(self.id)])


class Comment(models.Model):
    allgroups = models.ForeignKey(
        Allgroups,
        on_delete=models.CASCADE,
        related_name = 'comments',
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('allgroups_list')

class getUser(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )

class userList(models.Model):
    allgroups = models.ForeignKey(
        Allgroups,
        on_delete=models.CASCADE,
        related_name = 'userList',
        )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('allgroups_list')


