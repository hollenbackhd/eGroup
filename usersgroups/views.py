from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usersgroups

class GroupListView(ListView):
    model = Usersgroups
    template_name = 'group_list.html'

class GroupDetailView(DetailView):
    model = Usersgroups
    template_name = 'group_detail.html'

class GroupUpdateView(UpdateView):
    model = Usersgroups
    fields = ('title', 'body',)
    template_name = 'group_edit.html'

class GroupDeleteView(DeleteView):
    model = Usersgroups
    template_name = 'group_delete.html'
    success_url = reverse_lazy('group_list')

# Create your views here.
