from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def williamson(request):
    return HttpResponse('<h1> Williamson scores is 50 in world cricket semifinals')
def ravindra(request):
    return HttpResponse('<h1> ravindra is youngster </h1>')
