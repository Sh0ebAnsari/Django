from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
# def set_cookie(request):
#     res=render(request,'set_cookie.html')
#     res.set_cookie("name","ankit")
#     res.set_cookie("name","peter")
#     res.set_cookie("first_name","peter")
#     # res.set_cookie("last_name","max_age=5")
#     # res.set_cookie("last_name","max_age=10")
#     res.set_cookie("last_name","kumar",expires=datetime.utcnow()+timedelta(days=2))
#     return res 



# # getting cookies view 
# def get_cookie(request):
#     name=request.COOKIES['name']
#     first_name=request.COOKIES['first_name']
#     last_name=request.COOKIES['last_name']


#     name=request.COOKIES.get("name","Not found")
#     first_name=request.COOKIES['first_name']
#     last_name=request.COOKIES['last_name']
#     data={
#         "name":name,
#         "fn":first_name,
#         "ln":last_name,
#     }
#     return render(request,"get_cookie.html",data)


# # deleting cookies views

# def del_cookie(request):
#     res=render(request,'del_cookie.html')
#     res.delete_cookie("name")
#     res.delete_cookie("first_name")
#     res.delete_cookie("last_name")
#     return res



# creating signed cookie


# def set_signed_cookie(request):
#     res=render(request,'set_cookie.html')
#     # res.set_signed_cookie("name","ankit")
#     # res.set_signed_cookie("name","peter")
#     res.set_signed_cookie("first_name","peter")
#     res.set_signed_cookie("last_name","sho",salt="lastname")
#     # res.set_cookie("last_name","max_age=10")
#     res.set_signed_cookie("last_name","kumar",expires=datetime.utcnow()+timedelta(days=2))
#     return res 




# # getting signed cookies view 
# def get_signed_cookie(request):
#     name=request.get_signed_cookie['name',"not available"]
#     first_name=request.get_signed_cookie['first_name',"not available"]
#     last_name=request.get_signed_cookie['last_name',"not available"]


#     # name=request.get_signed_cookie.get("name","Not found")
#     # first_name=request.get_signed_cookie['first_name']
#     # last_name=request.get_signed_cookie['last_name']
#     data={
#         "name":name,
#         "fn":first_name,
#         "ln":last_name,
#     }
#     return render(request,"get_cookie.html",data)


# #  deleting signed cookies views

# def del_signed_cookie(request):
#     res=render(request,'del_cookie.html')
#     res.delete_cookie("name")
#     res.delete_cookie("first_name")
#     res.delete_cookie("last_name")
#     return res