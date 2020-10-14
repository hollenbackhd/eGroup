from django.views.generic import ListView
from .models import Usersgroups

class GroupListView(ListView):
    model = Usersgroups
    template_name = 'group_list.html'

# Create your views here.
