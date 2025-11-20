from django.shortcuts import render
from django.http import HttpResponse


"""
View will take in a repsonse as a param and return either a httpresponse or render a template
"""
# Create your views here.
def produceSector(request): 
    return render(request, 'home.html')  