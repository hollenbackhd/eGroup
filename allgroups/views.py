from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
    )
from django import forms
from django.db import models
from django.db.models import Model, F
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Allgroups, userlist, Comment, Comment1
from .forms import CommentForm



class AllgroupsListView(ListView):
    model = Allgroups
    template_name = 'allgroups_list.html'

    def isUser(val=None):
        return val

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
    model = (Allgroups)
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

    


    def allgroups_group(request, year, month, day, allgroups):
        allgroups = get_object_or_404(Allgroups, slug=allgroups,
                                  status='published',
                                  publish_year=year,
                                  publish_month=month,
                                  publish_day=day)
        comments1 = allgroups.comments1.filter(active=True)



        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.allgroups = allgroups
                new_comment.save()
            else:
                comment_form = CommentForm()
            return render(request,
                            'allgroups_detail.html',
                            {'group':allgroups,
                            'comments': comments1,
                            'comment_form': comment_form})

            
        

class userlistUpdateView(CreateView):
    model = userlist
    template_name = 'userlist_update.html'
    fields = ('allgroups',)
    success_url = reverse_lazy('allgroups_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_function(self):
        obj = self.get_object()
        return obj.Allgroups == Allgroups.author


class NewListUpdateView(CreateView):
    model = userlist
    fields=()
    template_name = 'userlist_newlist.html'
    success_url = reverse_lazy('allgroups_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def form_valid(self, form):
        form.instance.Allgroups = self.request.Allgroups
        return super().form_valid(form)
    

class userlistRemoveUserView(DeleteView):
    model = userlist
    template_name = 'userlist_removeuser.html'
    success_url = reverse_lazy('allgroups_list')
