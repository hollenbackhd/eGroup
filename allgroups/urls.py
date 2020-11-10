from django.urls import path
from .views import (
    AllgroupsListView,
    AllgroupsUpdateView,
    AllgroupsDetailView,
    AllgroupsDeleteView,
    AllgroupsCreateView,
    AllgroupsMygroupsView,
    AllgroupsRequestView,
    AllgroupsGroupView,
    )

urlpatterns = [
    path('<int:pk>/edit/', AllgroupsUpdateView.as_view(), name='allgroups_edit'),
    path('<int:pk>/request/', AllgroupsRequestView.as_view(), name='allgroups_request'),
    path('<int:pk>/', AllgroupsDetailView.as_view(), name='allgroups_detail'),
    path('<int:pk>/delete/', AllgroupsDeleteView.as_view(), name='allgroups_delete'),
    path('new/', AllgroupsCreateView.as_view(), name='allgroups_new'),
    path('mygroups/', AllgroupsMygroupsView.as_view(), name='allgroups_mygroups'),
    path('', AllgroupsListView.as_view(), name='allgroups_list'),
    path('<int:pk>/group/', AllgroupsGroupView.as_view(), name='allgroups_group'),

    ]
