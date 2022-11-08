from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there, and welcome to my Music App. We're gonna have tons of fun in this cohort")