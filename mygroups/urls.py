from django.urls import path
from .views import MygroupsDetailView
urlpatterns = [
    path('<int:pk>/', MygroupsDetailView.as_view(), name='mygroups_detail')
    ]
