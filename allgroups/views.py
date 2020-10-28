from django.contrib.auth.mixins import LoginRequiredMixin
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

class AllgroupsUpdateView(LoginRequiredMixin, UpdateView):
    model = Allgroups
    fields = ('title', 'body',)
    template_name = 'allgroups_edit.html'
    login_url = 'login'

class AllgroupsDeleteView(LoginRequiredMixin, DeleteView):
    model = Allgroups
    template_name = 'allgroups_delete.html'
    success_url = reverse_lazy('allgroups_list')
    login_url = 'login'

class AllgroupsCreateView(LoginRequiredMixin, CreateView):
    model = Allgroups
    template_name = 'allgroups_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
