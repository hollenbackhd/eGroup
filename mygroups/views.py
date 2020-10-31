from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.views.generic import DetailView
from django.urls import reverse_lazy

def MygroupsDetailView(DetailView):
    template_name = 'mygroups_detail.html'
