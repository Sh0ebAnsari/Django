from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Employee

def emp_data(request):
    emp_data=Employee.objects.all()
    return render(request,'home.html',{'data':emp_data})


def detail(request,pk):
    try:
        data=Employee.objects.get(id=pk)
    except Employee.DoesNotExist as derr:
        return HttpResponse("user of this id is not exist!!! try another")
    return render(request,"detail.html",{'data':data})   