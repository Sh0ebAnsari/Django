from django.shortcuts import render

# Create your views here.

def fees(request):
    title="fees"
    name="Python devloper"
    fees=2000000
    d={
        "tl":title,
        "nm":name,
        "fs":fees
    }
    return render(request,'enroll/fees.html',d)


def colleg(request):
    name="Abeda"
    student=2500
    d={
        "nm":name,
        "st":student
    }
    return render(request,'')