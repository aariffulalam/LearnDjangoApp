from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def runFirstApi(request):
    return HttpResponse('Hello i am first Api of this amazing journey for learn DJango')