from django.shortcuts import render

# Create your views here.
def home(request):
    name="python"
    age=25
    address="delhi"
    salary=540000
    d={
        'nm':name,
        'ag':age,
        'add':address,
        'sl':salary,
    }
    return render(request,'poll/home.html',context=d)

def index(request):
    cource_name="Backend dev"
    front='html'
    style="css"
    d={
        'server':cource_name,
        "f":front,
        "st":style,
    }
    return render(request,'poll/index.html',d)