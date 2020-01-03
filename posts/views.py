from django.shortcuts import render, HttpResponse

from django.http import Http404, HttpResponseRedirect, JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('Hi there')