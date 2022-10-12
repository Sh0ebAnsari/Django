from django.shortcuts import render

# Create your views here.

def home(request):
    title="working with static files"
    name="python"
    age=23
    address="delhi"
    d={
        'tl':title,
        'nm':name,
        'ag':age,
        'add':address,
    }
    return render(request,"poll/home.html",d)