from django.shortcuts import render

# Create your views here.
from .models import Post 
from django.core.paginator import Paginator
def home(request):
    # data=Post.objects.all()
    data=Post.objects.order_by('id')
    paginator=Paginator(data,per_page=2)
    print(paginator)

    page_no=request.GET.get('page')
    print(page_no)

    page_obj=paginator.get_page(page_no)
    print(page_obj)

    return render(request,"home.html",{"data":page_obj}) 