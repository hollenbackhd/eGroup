# Generated by Django 3.0.1 on 2020-11-16 05:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allgroups', '0014_remove_allgroups_userlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgroups',
            name='UserList',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]