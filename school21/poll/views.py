from django.shortcuts import render,HttpResponse
from .models import Employee
from django.db.models import Avg, Sum, Min , Max, Count, StdDev
# Create your views here.

def home(request):
    # data=Employee.objects.all()
    # print(data.query)

    # Method that do not return new QuerySet 
    # data=Employee.objects.get(id=1)
    try:
        # get()-query 
        # data=Employee.objects.get(name="ankit")
        # #  letest (queryset )
        # data=Employee.objects.latest("name")
        # data=Employee.objects.latest("joining date")
        # data=Employee.objects.latest("")

        # # earliest
        # data=Employee.objects.earliest("name")

        # # exiest
        # data=Employee.objects.all("")
        # data=Employee.objects.filter(name="rohit")
        # data=Employee.objects.filter(name="xyz")
        # print(data.exists())

        # # create()
        # data=Employee(
        #     name="xyz",
        #     roll=123, 
        #     city="pune", 
        #     salary=23344.6,
        #     joining_date="2016-02-04 02:01:33",
        #     address="india")

        # data=Employee(name="xyz",
        # roll=123,
        # city="pune",
        # salary=23344.6,
        # joining_date="2016-02-04 02:01:33",
        # address="india")

        # data=Employee(name="xyz",
        # roll=123, 
        # city="pune", 
        # salary=23344.6, 
        # joining_date="2016-02-04 02:01:33",
        # address="india")
        # # exact
        # data=Employee.objects.all()
        # data=Employee.objects.get(name__exact="Alex")
        # data=Employee.objects.get(name__exact="rohit")
        # data=Employee.objects.get(name__exact="Alex")
        # data=Employee.objects.get(name__exact="Alex")
        # data=Employee.objects.filter(name__exact="Alex")
        # data=Employee.objects.filter(name__iexact="Alex")
        # data=Employee.objects.filter(name__iexact="Shoeb")

        # # containes 

        
        # data=Employee.objects.get(name__contains="kumar")
        # data=Employee.objects.get(name__contains="Jha")
        # data=Employee.objects.filter(name__contains="Alex")

        # # in 
        # data=Employee.objects.filter(id__in=[2,3,4])
        # data=Employee.objects.filter(id__in=[2,3,4,5,8,6])
        # data=Employee.objects.filter(id__in=[2,3,4,5,8,6])


        # # gt and gte 
        # data=Employee.objects.filter(roll__gt='50')
        # data=Employee.objects.filter(roll__gt='150').order_by('name')
        # data=Employee.objects.filter(roll__gt='150').order_by('-id')
        # data=Employee.objects.filter(roll__gte='150').order_by('-id')
        # data=Employee.objects.filter(roll__gte='450').order_by('-id')

        # # lt and let 

        # data=Employee.objects.filter(roll__lt='450').order_by('-id')
        # data=Employee.objects.filter(roll__lte='450').order_by('-id')

        # # startswith and startswith
        # data=Employee.objects.filter(name__startswith="s")
        # data=Employee.objects.filter(name__startswith="p")
        # data=Employee.objects.filter(name__startswith="pin")
        # data=Employee.objects.filter(name__startswith="in")
        # data=Employee.objects.filter(address__startswith="IN")
        # data=Employee.objects.filter(address__startswith="iN")
         
        # # ends with and iends with 

        # data=Employee.objects.filter(address__endswith="r")
        # data=Employee.objects.filter(name__endswith="AR")
        # data=Employee.objects.filter(name__iendswith="ar")

        # # rang 
        # data=Employee.objects.filter(id__rang=(1,5))
        # data=Employee.objects.filter(joining_date__rang=("2016-04-16","2020-04-03"))
        # data=Employee.objects.filter(name__rang=("ankit","rohit"))
        # data=Employee.objects.filter(roll__rang=("100","150"))


        # # date


        # data=Employee.objects.filter(joining_date__date=(2016,6,22))
        # data=Employee.objects.filter(joining_date__date__gt=date(2010,6,22))
        # data=Employee.objects.filter(joining_date__date__gte=date(2010,6,22))
        # data=Employee.objects.filter(joining_date__date__lt=date(2010,6,22))
        # data=Employee.objects.filter(joining_date__date__lte=date(2010,6,22))

        # # year 
        # data=Employee.objects.filter(joining_date__year=2020)
        # data=Employee.objects.filter(joining_date__year__gt=2022)
        # data=Employee.objects.filter(joining_date__year__gte=2020)
        # data=Employee.objects.filter(joining_date__year__lt=2020)
        # data=Employee.objects.filter(joining_date__year__lte=2020)
        
        # # month 
        
        # data=Employee.objects.filter(joining_date__month=5)
        # data=Employee.objects.filter(joining_date__month__gt=10)
        # data=Employee.objects.filter(joining_date__month__gte=10)
        # data=Employee.objects.filter(joining_date__month__lt=10)
        # data=Employee.objects.filter(joining_date__month__lte=10)


        # # day
        
        # data=Employee.objects.filter(joining_date__day=2)
        # data=Employee.objects.filter(joining_date__day__gt=2)
        # data=Employee.objects.filter(joining_date__day__gte=2)
        # data=Employee.objects.filter(joining_date__day__lt=2)
        # data=Employee.objects.filter(joining_date__day__lte=2)


        # # time 

                
        # data=Employee.objects.filter(joining_date__time=time(4,12,50))
        # data=Employee.objects.filter(joining_date__time=time(4,12,50))
        # data=Employee.objects.filter(joining_date__time=time(4,12,50))
        # data=Employee.objects.filter(joining_date__time__gt=time(140))
        # data=Employee.objects.filter(joining_date__time__gte=time(4,12,50))
        # data=Employee.objects.filter(joining_date__time__lt=time(4,12,50))
        # data=Employee.objects.filter(joining_date__time__lte=time(4,12,50))

        # # hour 
        
        # data=Employee.objects.filter(joining_date__hour=14)
        # data=Employee.objects.filter(joining_date__hour=6)
        # data=Employee.objects.filter(joining_date__hour__gt=6)
        # data=Employee.objects.filter(joining_date__hour__gte=6)
        # data=Employee.objects.filter(joining_date__hour__lt=6)
        # data=Employee.objects.filter(joining_date__hour__lte=6)


        # # min 

        
        # data=Employee.objects.filter(joining_date__hour=14)
        # data=Employee.objects.filter(joining_date__hour=6)
        # data=Employee.objects.filter(joining_date__hour__gt=6)
        # data=Employee.objects.filter(joining_date__hour__gte=6)
        # data=Employee.objects.filter(joining_date__hour__lt=6)
        # data=Employee.objects.filter(joining_date__hour__lte=6)

                
        # # aggerate 
        data=Employee.objects.all()
        # print(data.aaggregate(Avg('roll'),Avg('salary')))
        # avg=data.aggregate(Avg('roll'),Avg('salary',distinct=True))
        # sum1=data.aaggregate(Avg('roll'),min('salary'))
        # sum1=data.annotate(Avg('roll'),min('salary'))
        # sum1=data.aaggregate(Count('roll'),Min('roll'),Max('salary'),Sum("roll"))
        # print(sum1)
        # print(data.count())


        # all at once 

        # sum1=data.aaggregate(Sum('roll'),Sum('salary'))
        # Avg=data.aaggregate(Avg('roll'),Avg('salary'))
        # min=data.aaggregate(Min('roll'),Min('salary'))
        # Max=data.aaggregate(Max('roll'),Max('salary'))
        # Count=data.aaggregate(Count('roll'),Count('salary'))
        # all_at=data.aggregate(
        #     Sum('roll'),Sum('salary'),
        #     Avg('roll'),Avg('salary'),
        #     Min('roll'),Min('salary'),
        #     Max('roll'),Max('salary'),
            
        # )
        # data={
        #     'sum':sum1,
        #     'avg':Avg,
        #     'min':min,
        #     "max":Max,
        #     'count':Count,
        #     'all':all_at,

        # }
        # data=Employee.objects.all()
        data=Employee.student.all()
        

    except Employee.MultipleObjectsReturn as merr:
        return HttpResponse("<html><h1>Multipal data return</h1></html>")
    except Employee.DoesNotExist as deer:
        return HttpResponse("<html><h1>Record Not Found in the Database!!check another </h1></html>")


    return render(request,'home.html',{'data':data})