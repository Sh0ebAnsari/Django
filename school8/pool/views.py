from django.shortcuts import render

# Create your views here.

def home(request):
    name="aniket"
    age=25
    address="mumbai"
    salary=500000
    d={
        "nm":name,
        "ag":age,
        "add":address,
        "sl":salary
    }

    return render(request,'pool/index.html',context=d)