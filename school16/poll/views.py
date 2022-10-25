from django.shortcuts import render
from .forms import register
# Create your views here.

def home(request):
    title='register'
    # fm=register(auto_id=True)
    # fm=register(auto_id=False)
    # fm=register(auto_id="id_%s",label_suffix=" ")
    fm=register(
        auto_id="id_%s",
        label_suffix="-",
        initial={
            'username':'ankit kumar',
            'email':'abc1234@gmail.com',
    }
    )
    # fm.order_fields(['email','username','password2','password1','age'])
    return render(request,'home.html',{'form':fm,'title':title})