from django.shortcuts import render

# Create your views here.
def home(request):
    title="Home page"
    name="Python"
    server="Django"
    client="Html"
    d={
        "tl":title,
        "nm":name,
        "ser":server,
        "cl":client,
    }
    return render(request,"poll/home.html",d)

