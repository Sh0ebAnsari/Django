from django.shortcuts import render,HttpResponse
from .forms import Register
# Create your views here.

def home(request):
    title='register'
    # fm=register(auto_id=True)
    # fm=register(auto_id=False)
    # fm=register(auto_id="id_%s",label_suffix=" ")
    # fm=register(
    #     auto_id="id_%s",
    #     label_suffix="-",
    #     initial={
    #         'username':'ankit kumar',
    #         'email':'abc1234@gmail.com',
    # }
    # )
    # fm.order_fields(['email','username','password2','password1','age'])
    # if request.method=='POST':
    #     fm=Register(request.POST)
    #     print("validation : ",fm.is_valid())
    #     print("Clening The Data".center(40,"*"))
    #     # print("User Name :" ,fm.cleaned_data['user_name'])
    #     # print("Email address :",fm.cleaned_data['email'])
    #     # print("Usre Age :",fm.cleaned_data['age'])
    #     # print("Password1 :",fm.cleaned_data['password1'])
    #     # print("Password2 :",fm.cleaned_data['password2'])
    #     # Or 
    #     print("User Name :" ,request.POST['user_name'])
    #     print("Email address :",request.POST['email'])
    #     print("Usre Age :",request.POST['age'])
    #     print("Password1 :",request.POST['password1'])
    #     print("Password2 :",request.POST['password2'])
    # else:
    #     fm=Register()
    
    # return render(request,'home.html',{'form':fm,'title':title})




    if request.method=='POST':
        fm=Register(request.POST)
        print("validation : ",fm.is_valid())
        print("Clening The Data".center(40,"*"))
        # print("User Name :" ,fm.cleaned_data['user_name'])
        # print("Email address :",fm.cleaned_data['email'])
        # print("Usre Age :",fm.cleaned_data['age'])
        # print("Password1 :",fm.cleaned_data['password1'])
        # print("Password2 :",fm.cleaned_data['password2'])
        # Or 
        print("User Name :" ,request.POST['user_name'])
        print("Email address :",request.POST['email'])
        print("Usre Age :",request.POST['age'])
        print("Password1 :",request.POST['password1'])
        print("Password2 :",request.POST['password2'])
        # return HttpResponse("Your account is created sucessfully!!{}")
        return render(request,'thanks.html')

    else:

        fm=Register()
    
    return render(request,'home.html',{'form':fm,'title':title})