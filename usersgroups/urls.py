from django.urls import path
from .views import (
    GroupListView,
    GroupUpdateView,
    GroupDetailView,
    GroupDeleteView,
    )
    
urlpatterns = [
    path('<int:pk>/edit/', GroupUpdateView.as_view(), name='group_edit'),
    path('<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),
    path('', GroupListView.as_view(), name='group_list'),
    ]
