from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Mygroups

class MygroupsDetailView(DetailView):
    model = Mygroups
