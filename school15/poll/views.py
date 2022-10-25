from audioop import reverse
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Employee,Customer

# def home(request):
    # # all
    # # data=Employee.objects.all()
    # data1=Employee.objects.all()
    # # data=Employee.objects.filter(emp_salary=1200000)
    # # data=Employee.objects.filter(emp_salary=12000)

    # # data1=Employee.objects.filter(group=True)
    # # data2=Employee.objects.filter(group=False)

    # # q1=data1.query
    # # q2=data2.query
    # # return render(request,'home.html',{'data1':data1,'data2':data2,"query1":q1,'query2':q2})

    # # exclude 
    # # data1=Employee.objects.exclude(group=True)
    # # data1=Employee.objects.exclude(group=False)
    # # data1=Employee.objects.exclude(group=False,emp_company='tcs')


    # # order_by
    # # data1=Employee.objects.order_by('id')
    # data1=Employee.objects.order_by('-emp_code')
    # # data1=Employee.objects.order_by('-joining_date')
    # data1=Employee.objects.order_by('group')
    # data1=Employee.objects.order_by('group').filter(group=True)
    # data1=Employee.objects.order_by('group').filter(emp_salary=1230000)

    # # reverse
    # data1=Employee.objects.order_by('emp_salary').reverse()
    # # data1=Employee.objects.order_by('emp_salary').reverse()[2:5]
    # data1=Employee.objects.order_by('id')[::-1]
    # data1=Employee.objects.order_by('id')[::-2]
    # data1=Employee.objects.order_by('id').reverse()[2:6:2]
    # q1=data1.query
    # print(data1.query)

    # value()
    # data1=Employee.objects.values()
    # data1=Employee.objects.values('id','emp_name','emp_code')
    # data1=Employee.objects.values('id','emp_name','emp_code','emp_address').order_by('-emp_name')
    
    
    # # distinct
    # data1=Employee.objects.distinct().values('emp_salary')

    # # values_list
    # data1=Employee.objects.values_list()
    # data1=Employee.objects.values_list('id','emp_address','emp_salary',named=True)[2:5]
    # data1=Employee.objects.values_list('id','emp_address','emp_salary',named=True)


    # # dates 
    # data1=Employee.objects.dates('joining_date','year',order='ASC')
    # # data1=Employee.objects.dates('joining_date','month',order='DESC')
    # # data1=Employee.objects.dates('joining_date','day',order='DESC')

    # print(data1)
    # query=data1.query


    # return render(request,'home.html',{'data1':data1,'query':query})


# def detail(request,pk):
#     try:
#         data=Employee.objects.get(id=pk)
#     except Employee.DoesNotExist as derr:
#         return HttpResponse("user of this id is not exist!!! try another")
#     return render(request,"detail.html",{'data':data})   


def home(request):

    data1=Employee



    return render(request,'home.html',{'data1':data1,'query':query})
