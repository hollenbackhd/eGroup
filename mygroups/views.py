from django.http import HttpResponse

def mygroupsView(request):
    return HttpResponse('My Groups')
