from django.shortcuts import render

# Create your views here
# views for seting session 

def set_session(request):
    request.session['name']="ankita"
    request.session['name']="ankur"
    return render(request,'session/set_session.html')

# views for setting session

def get_session(request):
    name1=request.session.get['name1',"not available"]
    address=request.session.get['address',"Address not available"]
    age=request.session.get['age',"Age not available"]

    d={
        "name":name1,
        "address":address,
        "age":age,
    }
    res=request.session.item()
    return render(request,"session/get_session.html",d)

# delete session view 
def del_session(request):
    # if "name" in request.session:
        # del request.session['name']
    
    res=request.session.flush()
    res=request.session.clear()
    return render(request,"session/del_session.html",{'res':res})