from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time

# Create your views here.
# function based views 
def home(request):
    tm=time.time()
    return HttpResponse("Hello welecome to Django !!!!!<hr><br><br> The time is:{}".format(tm))

def main(request):
    res="""
    <center>
    <ul style="list-style-type:none;">
        <li><a href="/home">Go Home</a></li>
        <li><a href="/index">Go Index</a></li>
        <li><a href="/page">Go Page</a></li>
        </ul>
        </center>
    """
    return HttpResponse(res)

def home(request):
    tm=datetime.datetime.now()
    return HttpResponse("""Hello Welecome to Django!!<hr><br><br>the time is :{},<a href="/main/">Go to main</a>""".format(tm))


def index(request):
    name="python"
    address="delhi"
    age=22
    fees=20000
    weight=20.39
    return HttpResponse("""
    Name is:{},<br><hr>
    Address is:{},<br><hr><br><hr>
    Age is:{},<br><hr>
    Student fees is :{},<br><hr>
    Student weight is:{}""".format(name,address,age,fees,weight))

def page(request,age,weight,color):
    nm=datetime.datetime.now()
    tm=nm.time()
    print("Age:",age)
    print("weight",weight)
    print("color:",color)
    return HttpResponse("""<h1>The Current Time is :{},Age:{},weight:{},color{}</h1><a href="/main">go Main</a>""".format(tm,age,weight,color))

from django.views.decorators.http import require_http_methods
@require_http_methods(["GET"])
def cource(request,Name,Address):
    a=20
    b=30
    res=a+b
    print("cource Name:",Name)
    print("Cource Address",Address)
    return HttpResponse("<h1>the sum of :{}and{}is:{},cource name :{},cource Address is:{}</h1>".format(a,b,res,Name,Address))



def asd(request):
    a=20
    b=30
    c=a-b
    return HttpResponse("sub is :{}".format(c))


