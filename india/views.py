from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<marquee><h1> virat 50th centuary in wc semi finals</h1></marqeee>')
def shreyas(request):
    return HttpResponse('<h1> shreyas scores is centuary in wc semifinals</h1>')