from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
    )

def index(request):
    return HttpResponse("My Groups")
