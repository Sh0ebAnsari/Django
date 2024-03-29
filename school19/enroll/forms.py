from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Choose Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name',"last_name","email"]
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control"}),
            'first_name':forms.TextInput(attrs={'class':"form-control"}),
            'last_name':forms.TextInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
        }



class UserEditForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')