from django.urls import path
from .views import mygroupsView

urlpatterns = [
    path('', mygroupsView, name='mygroups')

    ]
