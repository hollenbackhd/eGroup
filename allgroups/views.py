from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Allgroups

class AllgroupsListView(ListView):
    model = Allgroups
    template_name = 'allgroups_list.html'

class AllgroupsDetailView(DetailView):
    model = Allgroups
    template_name = 'allgroups_detail.html'

class AllgroupsUpdateView(UpdateView):
    model = Allgroups
    fields = ('title', 'body',)
    template_name = 'allgroups_edit.html'

class AllgroupsDeleteView(DeleteView):
    model = Allgroups
    template_name = 'allgroups_delete.html'
    success_url = reverse_lazy('allgroups_list')

class AllgroupsCreateView(CreateView):
    model = Allgroups
    template_name = 'allgroups_new.html'
    fields = ('title', 'body', 'author',)
