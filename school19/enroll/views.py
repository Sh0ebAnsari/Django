from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm ,SetPasswordForm
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect

from  django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm , UserEditForm


#User registration view
def sign_up(request):
    fm=SignUpForm()
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Your Account created")
            return redirect('/signup')
    else:
        fm=SignUpForm()
    return render(request,'enroll/signup.html', {'form':fm})

#User login view
def user_login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Hello Mr.{}-Welcome to Strange Application'.format(uname))
                return HttpResponseRedirect('/profile/')
    else:
        fm=AuthenticationForm()
    return render(request,'enroll/login.html',{'form':fm})

#user profile view
def user_profile(request):
    title="user profile page"
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'title':title})
    else:
        return HttpResponseRedirect("/login/")

#user logout view
def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect("/login/")


#password change with old password view
from django.contrib.auth import update_session_auth_hash
def changepassword(request):
    if request.user.is_authenticated:    
        if request.method=="POST":  
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password updated sucessfully!! ")
                return HttpResponseRedirect("/login/")
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepassword.html',{'form':fm})
    else:
        return HttpResponseRedirect("/login/")

# set new password view
def changepassword1(request):
    if request.method=="POST":
        fm=SetPasswordForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request," password updated sucessfully")
            return HttpResponseRedirect('/profile/')
    else:
        fm=SetPasswordForm(user=request.user)
    return render (request,'enroll/changepass1.html',{'from':fm})




# user Editing form view 
def user_profile(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=UserEditForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Profile updated sucessfully !!")
                UserEditForm()
        else:
            fm=UserEditForm(instance=request.user)
        return render(request,"enroll/profile.html",{'form':fm})
    else:
        return HttpResponseRedirect("/login")