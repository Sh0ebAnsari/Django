from django.shortcuts import render

# Create your views here.
def home(request,name):
    title="Url-pattern"
    # print("My Name  :",my_name)
    # print("My Name 2  :",my_name2)
    # print("Type:",type(my_name))
    # print("My id :-1",my_id)
    # print("My id Type:",type(my_id))

    # print("My id :-1",my_id1)
    # print("My id 1 Type:",type(my_id1))
    print("Name :  ",name)
    return render(request,'home.html',{'title':title,'name':name})
