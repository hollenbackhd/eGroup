from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django.db import models
from django.db.models import Model, F
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Allgroups, userlist, Comment


class AllgroupsListView(ListView):
    model = Allgroups
    template_name = 'allgroups_list.html'

class AllgroupsDetailView(DetailView):
    model = Allgroups
    template_name = 'allgroups_detail.html'

class AllgroupsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Allgroups
    fields = ('title', 'body','private',)
    template_name = 'allgroups_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AllgroupsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Allgroups
    template_name = 'allgroups_delete.html'
    success_url = reverse_lazy('allgroups_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class AllgroupsCreateView(LoginRequiredMixin, CreateView):
    model = Allgroups
    template_name = 'allgroups_new.html'
    fields = ('title', 'body','private',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AllgroupsMygroupsView(LoginRequiredMixin, ListView):
    model = Allgroups
    template_name = 'allgroups_mygroups.html'
    fields = ('title','body','private','request',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AllgroupsGroupView(DetailView):
    model = Allgroups
    template_name = 'allgroups_group.html'
    success_url = reverse_lazy('allgroups_list')

class userlistUpdateView(CreateView):
    model = userlist
    fields = ('user','allgroups',)
    template_name = 'userlist_update.html'
    success_url = reverse_lazy('allgroups_list')


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    


