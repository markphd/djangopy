from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from djangopy.settings import STATICFILES_DIRS
# from djangopy.settings import STATIC_ROOT


def home(request):
    return render(request, 'index.html')

static_files = STATICFILES_DIRS

def views(request):
    return HttpResponse(static_files)

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')
