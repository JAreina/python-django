from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def verPagina(request):
    return HttpResponse('<a href="https://github.com/JAreina">JAreina</a>')