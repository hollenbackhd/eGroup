from django.urls import path

from .views import HomePageView, MygroupsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('mygroups/', MygroupsView.as_view(), name='mygroups'),
    ]
