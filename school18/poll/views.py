from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
# Create your views here.


def home(request):
    title="Massage Framework"
    fm=UserForm(request.POST)
    if fm.is_valid():
        fm.save()
        messages.add_message(request,messages.SUCCESS,"Your form submitted")
        messages.add_message(request,messages.INFO,"Your form submitted")
        messages.add_message(request,messages.ERROR,"Your form submitted")
        messages.add_message(request,messages.WARNING,"Your form submitted")
        messages.add_message(request,messages.DEBUG,"Your form submitted")

    return render(request,'home.html',{'title':title,"form":fm})