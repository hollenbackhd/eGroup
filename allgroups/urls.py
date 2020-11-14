from django.urls import path, include
from .views import (
    AllgroupsListView,
    AllgroupsUpdateView,
    AllgroupsDetailView,
    AllgroupsDeleteView,
    AllgroupsCreateView,
    AllgroupsMygroupsView,
    userlistUpdateView,

    AllgroupsGroupView,
    )

urlpatterns = [
    path('<int:pk>/edit/', AllgroupsUpdateView.as_view(), name='allgroups_edit'),
    path('<int:pk>/', AllgroupsDetailView.as_view(), name='allgroups_detail'),
    path('<int:pk>/delete/', AllgroupsDeleteView.as_view(), name='allgroups_delete'),
    path('new/', AllgroupsCreateView.as_view(), name='allgroups_new'),
    path('mygroups/', AllgroupsMygroupsView.as_view(), name='allgroups_mygroups'),
    path('', AllgroupsListView.as_view(), name='allgroups_list'),
    path('<int:pk>/group/', AllgroupsGroupView.as_view(), name='allgroups_group'),
    path('<int:pk>/update/', userlistUpdateView.as_view(), name='userlist_update'),

    ]
