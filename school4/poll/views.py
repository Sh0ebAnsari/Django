from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    li="""
        <ul>
        <li><a href="/enroll/course/">cource</a></li>
        <li><a href="/enroll/fees/">fees</a></li>
        <li><a href="/enroll/enroll_new_data/">data</a></li>

        <li><a href="/poll/adm/">adm</a></li>
        <li><a href="/poll/poll_new_fees/">pool_feef</a></li>
        <li><a href="/poll/poll_new_data/">pool_data</a></li>

        </ul>
    
    """
    return HttpResponse(li)






# Create your views here.
def adm(request):
    name="JavaScript"
    address="mumbai"
    return HttpResponse("The name is :{}<br><br>,address is : {}".format(name,address))



def poll_fees(request):
    stu_fees=55000
    color_choice=['red','green','blue','black','purple','brown']
    return HttpResponse("<h1>Fees is :{},colors ia :{}</h1>".format(stu_fees,color_choice))


def poll_data(request):
    id={
        "stu1":122,
        "stu2":233,
        "stu3":345,
    }
    ph_no={10293847,84738327,8737636}
    return HttpResponse("<h2>Student id is: {},<br><br>Student contact  :{}</h1>".format(id,ph_no))
