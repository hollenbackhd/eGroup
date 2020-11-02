from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class MygroupsView(TemplateView):
    template_name = 'mygroups.html'
