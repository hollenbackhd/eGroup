from django.urls import path
from .views import MygroupsView

urlpatterns = [
    path('<int:pk>/', MygroupsDetailView.as_view(), name='mygroups_detail'),
    ]
