from turtle import title
from django.shortcuts import render

# Create your views here.

def home(request):
    title="Templates Inheritance"
    server="django"
    client="Html"
    db="Sqllite"
    d={
        'tl':title,
        'ser':server,
        'cl':client,
        'db':db
    }

    return render(request,'poll/home.html',d)



def index(request):
    title="index"
    return render(request,'poll/index.html',{'tl':title})



def course(request):
    title="course"
    return render(request,'poll/course.html',{'tl':title})


def fees(request):
    title="fees"
    return render(request,'poll/fees.html',{'tl':title})
