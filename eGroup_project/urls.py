from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('allgroups/', include('allgroups.urls')),
    path('mygroups/', include('mygroups.urls')),
    path('', include('pages.urls')),
    ]
