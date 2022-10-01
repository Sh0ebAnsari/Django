from django.shortcuts import render,HttpResponse

# Create your views here.


def sign_up(request):
    return HttpResponse("<h1>Hello Sign_up view from app application!!!</h1>")


def login(request):
    return HttpResponse("<h1>Hello Login view from app application!!!</h1>")