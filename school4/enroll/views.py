from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def course(request):
    name="python"
    address="delhi"
    return HttpResponse("The name is :{},address is : {}".format(name,address))



def enroll_fees(request):
    stu_name="ankit"
    age=20
    fees=2000
    return HttpResponse("<h1>Name is :{},Age is:{},and Fees is :{}</h1>".format(stu_name,age,fees))



def enroll_data(request):
    id={
        "stu1":122,
        "stu2":233,
        "stu3":345,
    }
    ph_no={10293847,84738327,8737636}
    return HttpResponse("<h2>Student id is: {},<br><br>Student contact  :{}</h1>".format(id,ph_no))