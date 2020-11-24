from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.db.models import CharField, Model
from django_mysql.models import ListCharField
from django.contrib.auth.models import User, Group
from django import forms, template

selectUser = get_user_model()
bestuserList = selectUser.objects.all()


class TrueFalse(models.Model):
    TF = models.TextField()

    def __str__(self):
        return self.TF

    def set(text):
        return text



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


class userlist(models.Model):
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


class SetVarNode(template.Node):
    def __init__(self, new_val, var_name):
        self.new_val = new_val
        self.var_name = var_name
    def render(self, context):
        context[self.var_name] = self.new_val
        return ''

    def setvar(parser,token):
        return SetVarNode(new_val[1:-1], var_name)


class Comment1(models.Model):
    allgroups = models.ForeignKey(Allgroups, on_delete=models.CASCADE, related_name='comments1')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.allgroups)




