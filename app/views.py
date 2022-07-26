from django.http import HttpResponse


def index(request):
    return HttpResponse("Made with Python. Hosted in Railway")
