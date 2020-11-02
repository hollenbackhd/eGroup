from django.urls import path
from .views import (
    AllgroupsListView,
    AllgroupsUpdateView,
    AllgroupsDetailView,
    AllgroupsDeleteView,
    AllgroupsCreateView,
    MygroupsView,
    )

urlpatterns = [
    path('<int:pk>/edit/', AllgroupsUpdateView.as_view(), name='allgroups_edit'),
    path('<int:pk>/', AllgroupsDetailView.as_view(), name='allgroups_detail'),
    path('<int:pk>/delete/', AllgroupsDeleteView.as_view(), name='allgroups_delete'),
    path('mygroups/', MygroupsView.as_view(),  name='mygroups_page'),
    path('new/', AllgroupsCreateView.as_view(), name='allgroups_new'),
    path('', AllgroupsListView.as_view(), name='allgroups_list'),
    ]
