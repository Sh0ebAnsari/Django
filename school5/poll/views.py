from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cource(request):
    return HttpResponse("<h1>Hello home applicationfrom poll </h1>")

def fees(request):
    return HttpResponse("<h1>Hello index view from poll application !!!</h1>")