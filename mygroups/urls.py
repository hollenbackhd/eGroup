from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import DetailView
from django.urls import revers_lazy
from .models import Mygroups


class Mygroups(DetailView):
    template_name = 'mygroups.html'
