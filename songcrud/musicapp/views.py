from django.shortcuts import render
from .models import Artiste, Song, Lyric
from rest_framework import viewsets

from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello there, and welcome to my Music App. We're gonna have tons of fun in this cohort")


#List all artistes

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all().order_by('first_name')
    serializer_class = ArtisteSerializer


#List all songs



#fetch a particular song 
#update a particular song (changing date or title)
#delete a particular song it (all fields)

